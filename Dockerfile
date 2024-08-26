FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./artefacts /code/artefacts

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app.py /code/app.py

EXPOSE 8000

CMD ["python", "app.py"]