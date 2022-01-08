FROM python:3.10

WORKDIR /usr/src/app

COPY requirement.txt .
RUN pip install -r requirement.txt

COPY . .
RUN python manage.py run server 0.0.0.0:8000