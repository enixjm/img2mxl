FROM python:3.8.5

WORKDIR /the/workdir/path
COPY . .
RUN pip install -r requirements.txt