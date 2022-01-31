FROM nginx:mainline-alpine
COPY nginx.conf /etc/nginx/templates/default.conf.template
