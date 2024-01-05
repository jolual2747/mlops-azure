FROM python:3.10

WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8081
EXPOSE 8080

CMD ["streamlit", "run", "--server.port", "8081", "app.py"]