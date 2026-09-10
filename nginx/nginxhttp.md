# 1. Create website directory
sudo mkdir -p /var/www/myapp
echo "<h1>My App</h1>" | sudo tee /var/www/myapp/index.html

# 2. Create config
sudo nano /etc/nginx/sites-available/myapp

# ဒီ content ကိုထည့်ပါ:
# server {
#     listen 80;
#     server_name myapp.com www.myapp.com;
#     root /var/www/myapp;
#     index index.html;
#     location / {
#         try_files $uri $uri/ =404;
#     }
# }

# 3. Enable
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/

# 4. Test and reload
sudo nginx -t 

# 5 if you want to do for sure dns 
sudo nano /etc/hosts
127.0.0.1  myapp.com www.myapp.com



sudo systemctl reload nginx
sudo systemctl reload nginx# 1. Create website directory
sudo mkdir -p /var/www/myapp
echo "<h1>My App</h1>" | sudo tee /var/www/myapp/index.html

# 2. Create config
sudo nano /etc/nginx/sites-available/myapp

# ဒီ content ကိုထည့်ပါ:
# server {
#     listen 80;
#     server_name myapp.com www.myapp.com;
#     root /var/www/myapp;
#     index index.html;
#     location / {
#         try_files $uri $uri/ =404;
#     }
# }

# 3. Enable
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/

# 4. Test and reload
sudo nginx -t
sudo systemctl reload nginx

# this is forwardproxy

