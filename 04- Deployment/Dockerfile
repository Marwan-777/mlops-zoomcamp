FROM python:3-alpine3.15

WORKDIR /app

COPY predict.py requirements.txt /app

RUN pip install -r requirements.txt

EXPOSE 3000

CMD ["python", "predict.py"]