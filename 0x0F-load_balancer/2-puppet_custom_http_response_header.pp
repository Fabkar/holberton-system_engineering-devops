#!/usr/bin/env bash
# Configure trought Puppet a header in Nginx server

exec { 'Header':
  command => 'sudo apt-get update';
  sudo apt-get -y install nginx;
  sudo sed -i "/server_name _/a add_header X-Server-By $hostname;" etc/nginx/site-available/default
  sudo service nginx restart',
  provider => 'shell',
}
