#!/bin/bash
_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
projectRoot="$_dir/.."
fqin="ghcr.io/eriknelson/synology-docker-poc"
pushd $projectRoot
docker build \
  --build-arg DOCKER_GROUP_ID=$(getent group docker | cut -d: -f3) \
  -f ./docker/Dockerfile \
  -t $fqin \
   .
popd
