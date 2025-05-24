#! /bin/bash

JRE_DIR=./jre

rm -rf $JRE_DIR
jlink \
    --add-modules java.base \
    --add-modules java.desktop \
    --add-modules java.instrument \
    --add-modules java.logging \
    --add-modules java.management \
    --add-modules java.naming \
    --add-modules java.net.http \
    --add-modules java.security.jgss \
    --add-modules jdk.zipfs \
    --compress zip-9 \
    --ignore-modified-runtime \
    --no-header-files \
    --no-man-pages \
    --output $JRE_DIR
