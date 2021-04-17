FROM python:alpine3.13
WORKDIR /app
COPY . .
expose 10000
CMD ["main.py"]
ENTRYPOINT ["python3"]