#sudo rename /home/box/web/etc/nginx.webconf /home/box/web/etc/nginx.conf
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/default


sudo /etc/init.d/nginx restart

#sudo rename /home/box/web/etc/helo.web /home/box/web/etc/hello
sudo ln -s /home/box/web/etc/hello   /etc/gunicorn.d/test

sudo /etc/init.d/gunicorn restart
#cd /home/box/web
#sudo gunicorn -w 3 -b 0.0.0.0:8080 -D hello:app

ps ax | grep nginx
ps ax | grep gunicorn

