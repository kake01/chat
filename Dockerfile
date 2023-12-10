FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# docker image build -t my-django-sqlite:v3 .
# docker image ls
# docker container run -p 8000:8000 コンテナID
