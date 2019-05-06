FROM python:3

RUN mkdir /code
COPY . /code
WORKDIR /code

RUN pip install -r requirements.txt
RUN python manage.py migrate
ENTRYPOINT ["python","manage.py","runserver","0:80"]

