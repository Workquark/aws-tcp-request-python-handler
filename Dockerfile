FROM python:alpine3.13
WORKDIR /app
COPY . .
CMD ["main.py"]
ENTRYPOINT ["python3"]