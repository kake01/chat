# gunicornが起動するか確認
* gunicorn chatBot2.wsgi:application -c gunicorn_config.py
* 起動できればsystemdを利用する
```
(base) a-kuma@akuma-VirtualBox:/etc/systemd/system\$ cat chatbot2.service
[Unit]
Description=Gunicorn instance to serve ChatBot
After=network.target
[Service]
User=a-kuma
Group=a-kuma
WorkingDirectory=/home/a-kuma/chatBot2/
ExecStart=/home/a-kuma/anaconda3/bin/gunicorn chatBot2.wsgi:application -c /home/a-kuma/chatBot2/gunicorn_config.py
[Install]
WantedBy=multi-user.target
```
(base) a-kuma@akuma-VirtualBox:/etc/systemd/system$ sudo systemctl enable chatbot2
(base) a-kuma@akuma-VirtualBox:/etc/systemd/system$ sudo systemctl start chatbot2
(base) a-kuma@akuma-VirtualBox:/etc/systemd/system$ sudo systemctl status chatbot

# nginxの設定
(base) a-kuma@akuma-VirtualBox:/etc/nginx/sites-available\$ cat /etc/nginx/nginx.conf
```
user a-kuma;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/\*.conf;
events {
worker_connections 768; # multi_accept on;
}
http {

    # Basic Settings
    sendfile on;
    tcp_nopush on;
    types_hash_max_size 2048;

    # server_tokens off;
    # server_names_hash_bucket_size 64;
    # server_name_in_redirect off;
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # SSL Settings
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
    ssl_prefer_server_ciphers on;

    # Logging Settings
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    # Virtual Host Configs
    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}
```

sudo ln -s /etc/nginx/sites-available/chatBot2 /etc/nginx/sites-enabled
(base) a-kuma@akuma-VirtualBox:/etc/nginx/sites-available\$ cat chatBot2
```
# /etc/nginx/sites-available/myproject

server {
listen 80;
server_name hostname -I の値;
location = /favicon.ico { access_log off; log_not_found off; }
location /static/ {
alias /home/a-kuma/chatBot2/static/;
autoindex on;
error_page 403 /error403.html;
}
location / {
include proxy_params;
proxy_pass http://0.0.0.0:8000; # Gunicorn がリッスンしているアドレスとポートに合わせて設定
}
}
```

# 困った際のチートシート
* nginxで80ポートが使われてそうなエラーが出たら
* * sudo lsof -i :80
* * sudo kill -9 <PID>
* nginxでそれ以外で困った場合には下記のコマンドで対応すべし
* * cat /var/log/nginx/error.log
* * systemctl status nginx.service
* * journalctl -xeu nginx.service

