#!/bin/bash

cd /home/neil/product_review

# build static for django
source /home/neil/anaconda3/bin/activate product_review
python product_review/manage.py collectstatic
cp -r /home/neil/product_review/product_review/static/* /home/neil/product_review/static/

# Build the frontend and move to dist files
docker build -f frontend/Dockerfile -t product_review_frontend:0 /home/neil/product_review/frontend/
docker run -it -v /home/neil/product_review/frontend:/app product_review_frontend:0 npm run build
cp -r /home/neil/product_review/frontend/dist/* /home/neil/product_review/static/

# build the images
export DOCKER_BUILDKIT=1
docker compose build
