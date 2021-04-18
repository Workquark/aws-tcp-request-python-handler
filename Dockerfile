FROM python:alpine3.13
WORKDIR /app
COPY . .
expose 10000
CMD ["-u", "main.py"]
ENTRYPOINT ["python3"]