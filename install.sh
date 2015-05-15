#!/bin/bash

# Установка необходимых компонентов для RHEL7
sudo yum -y check-update
sudo yum groupinstall -y development
sudo yum -y install bash-completion zlib-dev openssl-devel sqlite-devel bzip2-devel xz-libs nmap mc nano git

# Выключение SELinux

# Установка Python
wget http://www.python.org/ftp/python/3.3.3/Python-3.3.3.tar.xz
xz -d Python-3.3.3.tar.xz
tar -xvf Python-3.3.3.tar
cd Python-3.3.3    
./configure
make
make install

# Установка компонентов Python
sudo pip3 install virtualenv pillow uwsgi psycopg2

# Установка компонентов Django
sudo pip3 install django django-admin-bootstrapped django-summernote django-classy-tags

# Настройка uwsgi
sudo mkdir /var/log/uwsgi/
sudo touch /var/log/uwsgi/santech.log
sudo mkdir /etc/uwsgi/
sudo mkdir /etc/uwsgi/vassals/
sudo ln -s uwsgi.ini /etc/uwsgi/vassals/
sudo cp uwsgi.service /etc/systemd/system/
sudo systemctl enable uwsgi.service
sudo systemctl start uwsgi.service

# Настройка Nginx
sudo yum -y install nginx
sudo ln -s site_nginx.conf /etc/nginx/sites-enabled/
sudo systemctl enable nginx.service
sudo systemctl start nginx.service

# Настройка PostgreSQL
sudo yum -y install postgresql postgresql-libs postgresql-server postgresql-contrib

sudo systemctl enable postgresql.service
sudo systemctl start postgresql.service
sudo initdb --locale en_US.UTF-8 -E UTF8 -D '/var/lib/pgsql/data'
sudo nano /var/lib/pgsql/data/postgresql.conf # listen_addresses = '*', port = 5432, password_encryption = on
sudo nano /var/lib/pgsql/data/pg_hba.conf # host all all 89.22.178.54/32 md5
sudo -i -u postgres
psql
ALTER USER postgres WITH PASSWORD '14875264';
sudo systemctl restart postgresql.service
