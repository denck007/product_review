
FROM python:3.9-slim

# Install all the requirements
WORKDIR /product_review
COPY . /product_review/
RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt
