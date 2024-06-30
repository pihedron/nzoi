{ pkgs, ... }: {
  channel = "stable-23.11"; # or "unstable"
  packages = [
    pkgs.python3
    pkgs.clang
    pkgs.adoptopenjdk-bin
  ];
  env = {};
  idx = {
    extensions = [
      "ms-python.debugpy"
      "ms-python.python"
    ];
    previews = {
      enable = true;
      previews = {};
    };
    workspace = {
      onCreate = {};
      onStart = {};
    };
  };
}
