FROM mysql:8.0.27
ENV MYSQL_DATABASE vaccination_db
ENV MYSQL_USER root
ENV MYSQL_PASSWORD root
COPY vaccination_db.sql /docker-entrypoint-initdb.d/
EXPOSE 3306
