FROM python:3.8.12-slim

RUN apt-get update -y

RUN apt-get install tk -y

COPY . .

CMD ["main2.py"]
ENTRYPOINT ["python3"]