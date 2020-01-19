# Use the Nginx image
FROM nginx:stable

COPY index.html /usr/share/nginx/html/

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf


# Replace with our own nginx.conf
# COPY ssl.conf /etc/nginx/conf.d/ssl.conf

COPY nginx.conf /etc/nginx/conf.d/

COPY ssl.csr /etc/nginx/ssl.csr
COPY ssl.key /etc/nginx/ssl.key

EXPOSE 443