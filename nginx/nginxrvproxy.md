you check first 
/etc/nginx/nginx.conf
include /etc/nginx/conf.d/*.conf;
that is allow or no 


second 
you can create .conf under  /etc/nginx/conf.d/*(what ever you want to give).conf

this is .conf file 
server {
listen 80;
server_name nssl.example.com;
acess_log /var/log/nginx/nssl_acess.log
error_log /var/log/nginx/nssl_error.log
location / {
 proxy_pass http://laravel.com;#(this is example and you can put any web you want to)
 
}
}

third 
sudo chown -R $USER:$Group /etc/nginx/conf.d
sudo chmod -R 755 /etc/nginx/conf.d

fourth
sudo nano /etc/hosts
and you add 127.0.0.1  nssl.example.com ( )

# now you call http://nssl.example.com  and it go to 
#  reverse proxy ( http://laravel.com)