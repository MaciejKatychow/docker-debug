FROM python:3.11
WORKDIR /app
COPY app.py .
RUN pip install debugpy
RUN pip install flask
CMD ["python", "app.py"]