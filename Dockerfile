FROM python:3.4

WORKDIR /code

ADD django_code /code

RUN pip3 install -r requirements.txt

CMD python3 manage.py runserver 0.0.0.0:8000

EXPOSE 8000