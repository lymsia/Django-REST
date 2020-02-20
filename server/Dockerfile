FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT=dev

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8080"]
