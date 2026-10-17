# Основа для образа
FROM ubuntu:22.04
 
# Установка зависимостей
RUN apt update && apt install -y python3 python3-pip
RUN pip install Flask
 
# Копирование приложения в образ
COPY hello.py /
 
# Конфигурация Flask
ENV FLASK_APP=hello
EXPOSE 8000
CMD flask run --host 0.0.0.0 --port 8000
