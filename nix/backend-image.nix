{ pkgs }:
let 
  pythonEnv = pkgs.python314.withPackages (ps: with ps; [
    numpy pandas scikit-learn
    fastapi uvicorn joblib
  ]);

  appFiles = pkgs.runCommand "nako-backend-files" {} ''
    mkdir -p $out/app/src $out/app/models
    cp -r ${../src/nako} $out/app/src/nako
    cp ${../models/vulnerability_model.joblib} \
      $out/app/models/vulnerability_model.joblib

    find $out -type d -name __pycache__ \
      -prune -exec rm -rf {} +
  '';

in pkgs.dockerTools.buildLayeredImage {
  name = "nako-backend";
  tag = "latest";
  contents = [
    pythonEnv
    appFiles
  ];
  config = {
    WorkingDir = "/app";
    Cmd = [
      "${pythonEnv}/bin/python3.14"
      "-m"
      "uvicorn"
      "nako.api:app"
      "--app-dir"
      "/app/src"
      "--host"
      "0.0.0.0"
      "--port"
      "8000"
    ];
    ExposedPorts = {
      "8000/tcp" = {};
    };
  };
}
