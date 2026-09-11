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



#### error fix feature (for subpage)

server {
    listen 80;
    server_name nssl.com;

    # 1. Main Application - Laravel (Port 8000 ဆိုပါစို့)
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
       
    }

   # 2
   location = /subpage {
        proxy_pass http://127.0.0.1:8000/apitest-form;
        proxy_set_header Host $host;
       
    }

    # 3. Python / Flask Application (Port 5000)
    # /python/subpage ဟု ခေါ်ပါက Python ဘက်သို့ /subpage အဖြစ်သာ ရောက်ရှိမည်
    location /python/ {
        proxy_pass http://127.0.0.1:5000/;   # အဆုံးတွင် / ပါရပါမည်
        proxy_set_header Host $host;
        
    }

}


သီးခြား Subdomain ဖြင့် ခွဲခြားနည်း (အကောင်းဆုံး နည်းလမ်း)
URL Path (/python/) ဖြင့် မခွဲချင်ဘဲ Subdomain ဖြင့် ခွဲသုံးပါက Routing ရှုပ်ထွေးမှု လုံးဝမရှိတော့ပါ။

Nginx
# 1. Laravel (nssl.com)
server {
    listen 80;
    server_name nssl.com;

    location / {
        proxy_pass http://127.0.0.1:8000; # Laravel Port
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

# 2. Python Flask (py.nssl.com)
server {
    listen 80;
    server_name py.nssl.com;

    location / {
        proxy_pass http://127.0.0.1:5000; # Python Port
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}