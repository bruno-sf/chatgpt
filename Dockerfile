FROM python:3.9-slim

ARG API_VALUE

ENV OPENAI_API_KEY=$API_VALUE

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "python_chatgpt.py"]