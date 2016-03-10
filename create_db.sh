mysql -uroot -e "CREATE DATABASE askdb CHARACTER SET utf8;"
mysql -uroot -e "CREATE USER 'stepic'@'localhost' IDENTIFIED BY 'stepic';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON askdb.* TO 'stepic'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
