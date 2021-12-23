FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/

COPY nginx.key /etc/nginx/
COPY nginx.crt /etc/nginx/