FROM kauvinl/spark-base/spark-py:1.0
USER root
WORKDIR /app
COPY app/main.py .