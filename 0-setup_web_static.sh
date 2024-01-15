#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm;
    add_header X-Served-By $HOSTNAME;

    location /hbnb_static {
	alias /data/web_static/current;
	index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location /404 {
        root /etc/nginx/html;
        internal;
    }
}" > /etc/nginx/sites-available/default

nginx -t 
sudo service nginx restart
