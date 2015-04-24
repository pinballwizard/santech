#!/bin/bash

# Установка необходимых компонентов для RHEL7
sudo yum -y check-update
sudo yum -y install bash-completion

# Настройка uwsgi
sudo mkdir /var/log/uwsgi/
sudo touch /var/log/uwsgi/santech.log
sudo mkdir /etc/uwsgi/
sudo mkdir /etc/uwsgi/vassals/
sudo ln -s uwsgi.ini /etc/uwsgi/vassals/
sudo cp uwsgi.service /etc/systemd/system/


# Настройка Nginx
sudo ln -s site_nginx.conf /etc/nginx/sites-enabled/
