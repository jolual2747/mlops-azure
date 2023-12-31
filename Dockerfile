FROM python:3.10

WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8080"]