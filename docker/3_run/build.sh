#!/usr/bin/env bash

cp ../../requirements.txt .;
docker build -t armadillica/grafista -f run.docker .;
rm requirements.txt;
