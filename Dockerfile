# FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-runtime

# RUN apt update && apt install -y libgl1-mesa-glx libglib2.0-0

# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential && \
#     rm -rf /var/lib/apt/lists/*

# COPY requirements.txt .
# RUN pip install -r requirements.txt
# COPY bfaaap/yolov5/requirements.txt .
# RUN pip install -r requirements.txt

# WORKDIR /usr/src/app

# # Copy contents
# COPY . /usr/src/app

# CMD python ./app2.py




FROM public.ecr.aws/lambda/python:3.8

COPY . .

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["app.handler"]      