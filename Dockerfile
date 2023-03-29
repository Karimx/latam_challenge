#FROM python:3.10-slim-buster
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY end_point /app/end_point
COPY inference_server /app/inference_server
COPY resources /app/resources

EXPOSE 80

# Start the FastAPI app
CMD ["uvicorn", "end_point.main:app", "--host", "0.0.0.0", "--port", "80"]
# uvicorn end_point.main:app --host 0.0.0.0 --port 80

