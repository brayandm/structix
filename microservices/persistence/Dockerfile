FROM python:3.13-alpine

WORKDIR /app

RUN pip install pymysql cryptography

COPY server.py .

EXPOSE 3000

CMD ["python", "server.py"]