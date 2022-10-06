FROM python:3.8.10
ENV PYTHONUNBUFFERED=1
WORKDIR /test_task
COPY requirements.txt /test_task/
RUN pip install -r requirements.txt
COPY . /test_task/
