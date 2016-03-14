mysql -uroot -e "CREATE DATABASE askdb CHARACTER SET utf8;"
mysql -uroot -e "CREATE USER 'stp'@'localhost' IDENTIFIED BY 'stp';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON askdb.* TO 'stp'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
