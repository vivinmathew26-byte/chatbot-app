FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN python -m spacy download en_core_web_sm

COPY app.py .
COPY templates/ templates/

EXPOSE 5000

CMD ["python", "app.py"]
