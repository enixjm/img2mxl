*To produce a musicxml file from a sheet music image (You must comply with and are also resibonsible for copyright laws, etc. for use of sheet music images in img2Mxml)

## Description
 악보 이미지(.jpg 또는 .png)를 XML 형식으로 표기하는 MusicXML(.mxl 또는 .musicxml) 포멧으로 변환할 수 있음

## Usage
 YOLO v5 모델(stored at "yolov5/weightsstock/")을 추가로 훈련하려면 
 makeyolomusicdict/generatedictforxml.py의 429~474행에 명시된 특정 레이블로 각 모델을 확인

### Environment
 Mac, Python==3.8.5, YOLO v5
 Docker 20.10.7 Flask 1.1.2

### yolo place yolov5 weights in /bfaap.yolov5/weightsstock/
    
    mkdir bfaaap/yolov5/weightsstock
    cd bfaaap/yolov5/weightsstock
    wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1hTrPCL30Xbi9-qHyqb2lAcI_FoFdk0HK' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1hTrPCL30Xbi9-qHyqb2lAcI_FoFdk0HK" -O img2xml_weights.zip && rm -rf /tmp/cookies.txt
    unzip img2xml_weights.zip



Todo
- [ ] support in pdf format.
- [ ] build pipeline Apache Airflow.
- [ ] detection rate for all music symbol
