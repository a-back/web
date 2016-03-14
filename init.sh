#----- Common -----
sudo apt-get update
sudo apt-get install mc

#----- Nginx -----
sudo rm /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf

sudo /etc/init.d/nginx restart

#----- Gunicorn -----
sudo rm /etc/gunicorn.d/*.*
sudo ln -s /home/box/web/etc/hello   /etc/gunicorn.d/test
sudo ln -s /home/box/web/etc/django   /etc/gunicorn.d/django

sudo /etc/init.d/gunicorn restart
#cd /home/box/web
#sudo gunicorn -w 3 -b 0.0.0.0:8080 -D hello:app

#----- MySQL -----
sudo /etc/init.d/mysql restart

#----- Test of run -----
ps ax | grep nginx
ps ax | grep gunicorn
ps ax | grep mysql

#----- BD + superuser (web) -----
./create_db.sh

#----- Validate + syncdb -----
cd ask
./manage.py validate
#./manage.py sybcdb