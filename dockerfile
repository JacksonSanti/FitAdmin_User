FROM python:3.9-slim

WORKDIR /users

COPY requirements.txt /users/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 50051

CMD ["python", "server_grpc.py"]
