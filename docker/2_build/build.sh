#!/usr/bin/env bash

mkdir -p ../3_run/wheelhouse;
cp ../../requirements.txt .;

docker build -t grafista_build -f build.docker .;
docker run --rm \
       -v "$(pwd)"/../3_run/wheelhouse:/data/wheelhouse \
       grafista_build;

rm requirements.txt;
