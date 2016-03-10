sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql restart

ps ax | grep nginx
ps ax | grep gunicorn
ps ax | grep mysql
