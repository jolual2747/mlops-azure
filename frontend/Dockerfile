FROM python:3.10

WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 80

CMD ["streamlit", "run", "--server.port", "80", "app.py"]