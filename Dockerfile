FROM ultralytics/yolov5

RUN pip install -r requirements.txt

RUN rm -rf /usr/src/app
WORKDIR /usr/src

# Copy contents
COPY . /usr/src

EXPOSE 5000

CMD python ./app.py