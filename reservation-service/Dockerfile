FROM python:3.13-slim

WORKDIR /app

COPY reservation_service/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY reservation_service/ .

EXPOSE 8083

CMD ["python", "manage.py", "runserver", "0.0.0.0:8083"]