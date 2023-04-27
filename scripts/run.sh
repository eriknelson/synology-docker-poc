#!/bin/bash
_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
rootDir="$_dir/.."
fqin="ghcr.io/eriknelson/synology-docker-poc"
cmd=$1

if [[ "$cmd" == "" ]]; then
  echo "ERROR: Must pass cmd to run"
  exit 1
fi

docker run --rm -it \
  --env SDP_VOL_SRC_DIR="$(pwd)/docker/run" \
  -v /var/run/docker.sock:/var/run/docker.sock \
  $fqin $cmd
