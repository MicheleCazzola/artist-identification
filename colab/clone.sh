#/usr/bin/bash

REPO=$1
FOLDER_NAME=$2

git config --global core.compression 0
git config --global pack.windowMemory 100m
git config --global pack.packSizeLimit 100m
git config --global index.threads 4

git clone $REPO $FOLDER_NAME --progress --verbose
cd $FOLDER_NAME; git pull --all

git status

exit 1