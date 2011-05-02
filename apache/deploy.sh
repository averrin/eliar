echo "Copy .conf to Apache conf.d"
sudo cp ./*.conf /etc/apache2/conf.d/
echo "Restart Apache"
sudo /etc/init.d/apache2 restart
