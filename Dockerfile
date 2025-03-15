FROM python:3.11

WORKDIR /flask-app

COPY requirements.txt /flask-app/

COPY app/api.py app/database.py app/configuration.py /flask-app/
COPY config.json /flask-app/
COPY config /flask-app/config/

RUN pip install -r requirements.txt

EXPOSE 5050

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5050", "api:app"]