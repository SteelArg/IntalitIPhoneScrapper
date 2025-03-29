FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/

# COPY app/api.py app/database.py app/configuration.py /flask-app/app/
COPY config.json /app/
COPY config/ /app/config/

RUN pip install -r requirements.txt

EXPOSE 5050

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5050", "api:app"]