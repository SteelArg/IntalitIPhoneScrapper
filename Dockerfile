FROM python:3.11

WORKDIR /flask-app

COPY requirements.txt /flask-app/

COPY app/api/api.py /flask-app/app/api/
COPY app/database.py app/configuration.py app/__init__.py /flask-app/app/
COPY app/model/ /flask-app/app/model/

COPY app/utils/ /flask-app/app/utils/

COPY config.json /flask-app/
COPY config/ /flask-app/config/

RUN pip install -r requirements.txt

EXPOSE 5050

CMD ["gunicorn", "-w", "4", "--pythonpath", "/flask-app", "-b", "0.0.0.0:5050", "app.api.api:app"]