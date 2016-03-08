sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart

ps ax | grep nginx
ps ax | grep gunicorn

