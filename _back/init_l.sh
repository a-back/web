sudo ln -s /home/bitnami/Stepic/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/bitnami/Stepic/web/etc/hello.py   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
