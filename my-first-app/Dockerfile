# Use the official Nginx image from Docker Hub as the base image
# FROM nginx:latest

# Copy the custom index.html file from the current directory on the host
# into the default Nginx web root directory inside the image.
# COPY index.html /usr/share/nginx/html

FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /app /app
ENTRYPOINT ["python", "hello.py"]
