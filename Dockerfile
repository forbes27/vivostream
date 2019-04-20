FROM python:2.7

COPY ./ /app

WORKDIR /app

EXPOSE 5000

ENV FLASK_CONFIG=development
ENV FLASK_APP=run.py

RUN pip install -r requirements.txt

CMD ["python", "run.py"]



