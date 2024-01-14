#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '/\/hbnb_static {/d' /etc/nginx/sites-available/default
echo -e "\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n}" | sudo tee -a /etc/nginx/sites-available/default
nginx -t
sudo service nginx restart