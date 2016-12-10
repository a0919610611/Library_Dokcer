#!/bin/sh
envsubst < nginx.tmpl > /etc/nginx/nginx.conf
nginx -g "daemon off;"
