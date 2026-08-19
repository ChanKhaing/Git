# FROM php:8.2-fpm မှ php:8.3-fpm သို့ ပြောင်းရန်
FROM php:8.4-fpm
# Working Directory သတ်မှတ်ခြင်း
WORKDIR /var/www

# Laravel အတွက် လိုအပ်သော PHP Extensions များ Install လုပ်ခြင်း
RUN apt-get update && apt-get install -y \
    build-essential \
    libpng-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    locales \
    zip \
    jpegoptim optipng pngquant gifsicle \
    vim \
    unzip \
    git \
    curl \
    libonig-dev \
    libzip-dev \
    && docker-php-ext-install pdo_mysql mbstring zip exif pcntl

# Composer ထည့်သွင်းခြင်း
COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer

# Application Code များကို Copy ကူးခြင်း
COPY . /var/www

EXPOSE 9000
CMD ["php-fpm"]
