FROM python:3.11.1-alpine3.17
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 5000
VOLUME /code/logs
CMD python manage.py runserver 0.0.0.0:5000