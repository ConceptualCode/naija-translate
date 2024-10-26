FROM python:3.10-slim

WORKDIR /app

COPY ./src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./model /app/model

COPY ./src /app/src

WORKDIR /app/src

EXPOSE 7860

CMD ["uvicorn", "apis:app", "--host", "0.0.0.0", "--port", "7860"]