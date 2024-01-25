FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
RUN mkdir -p /var/www/.well-known/acme-challenge
RUN mkdir -p /var/www/