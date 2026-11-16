
{
  description = "Nako - Python vulnerability detection";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/02f754064dce1a8c2b4b301f25c43b44fe2bbfd";

    flake-utils = {
      url = "github:numtide/flake-utils/cd489559845d81f673a12885576016c65cbe9363";
    };
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };

        mkPythonEnv = { extraPackages ? (_: []) }:
          pkgs.python314.withPackages (ps: with ps; [
            numpy
            pandas
            scikit-learn
          ] ++ extraPackages ps);

        devPython = mkPythonEnv {
          extraPackages = ps: with ps; [
            ipython
            matplotlib
            openpyxl
            seaborn
            fastapi
            uvicorn
            joblib
          ];
        };

        containerTools =
          pkgs.lib.optionals pkgs.stdenv.hostPlatform.isLinux [
            pkgs.podman
            pkgs.podman-compose
          ];

        # Docker-compatible container images are Linux outputs.
        containerPackages =
          if pkgs.stdenv.hostPlatform.isLinux then {
            backend = import ./nix/backend-image.nix {
              inherit pkgs;
            };

            frontend = import ./nix/frontend-image.nix {
              inherit pkgs;
            };

            fakeNss = pkgs.dockerTools.fakeNss;
          } else {};
      in
      {
        packages = containerPackages // {
          nginx = pkgs.nginx;
        };

        devShells.default = pkgs.mkShell {
          packages = [
            devPython
            pkgs.browser-sync
            pkgs.nginx
          ] ++ containerTools;
        };
      }
    );
}

