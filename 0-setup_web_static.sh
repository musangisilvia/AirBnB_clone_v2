#!/usr/bin/env bash

# install nginx if not installed

sudo apt-get update
sudo apt-get install -y nginx

# create folders if they don't exist
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/

# create dummy html file
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# create symbolic link
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current

# chown of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# update nginx confi to serve content of /data/web_static/current to hbnb_static
sudo sed -i '39i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

# restart nginx
sudo service nginx restart
