server {
    listen 80;
    server_name kennekslots.com www.kennekslots.com;

    # Redirect HTTP to HTTPS
    return 301 https://$host$request_uri;

    # Location block for favicon.ico
    location = /favicon.ico {
        access_log off;
        log_not_found off;
    }

    # Location block for static files
    location /static/ {
        alias /var/www/kennekslots/static/;
    }

    # Location block for media files
    location /media/ {
        alias /var/www/kennekslots/media/;
    }

    # Location block for proxying requests to Django
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
