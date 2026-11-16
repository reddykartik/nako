
{ pkgs }:

let
  webFiles = pkgs.runCommand "nako-frontend-files" {} ''
    mkdir -p $out/usr/share/nginx/html
    mkdir -p $out/etc/nginx/conf.d
    mkdir -p $out/tmp
    mkdir -p $out/var/log/nginx
  
    cp -r ${../web}/. $out/usr/share/nginx/html/
    cp ${../deploy/nginx.conf} \
      $out/etc/nginx/conf.d/default.conf
  '';
  nginxConf = pkgs.writeText "nginx.conf" ''
    user nobody nobody;
    worker_processes auto;
    pid /tmp/nginx.pid;
    error_log stderr;

    events {}

    http {
      include ${pkgs.nginx}/conf/mime.types;
      default_type application/octet-stream;

      access_log /dev/stdout;

      sendfile on;

      client_body_temp_path /tmp/client_body;
      proxy_temp_path /tmp/proxy_temp;
      fastcgi_temp_path /tmp/fastcgi_temp;
      uwsgi_temp_path /tmp/uwsgi_temp;
      scgi_temp_path /tmp/scgi_temp;

      include /etc/nginx/conf.d/*.conf;
    }
  '';

in
pkgs.dockerTools.buildLayeredImage {
  name = "nako-frontend";
  tag = "latest";

  contents = [
    pkgs.nginx
    pkgs.dockerTools.fakeNss
    webFiles
  ];

  config = {
    Cmd = [
      "${pkgs.nginx}/bin/nginx"
      "-c"
      "${nginxConf}"
      "-g"
      "daemon off;"
    ];

    ExposedPorts = {
      "80/tcp" = {};
    };
  };
}

