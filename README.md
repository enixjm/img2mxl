# yolo place yolov5 weights in /bfaap.yolov5/weightsstock/
    
    !mkdir /content/img2xml/bfaaap/yolov5/weightsstock
    %cd /content/img2xml/bfaaap/yolov5/weightsstock
    !wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1hTrPCL30Xbi9-qHyqb2lAcI_FoFdk0HK' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1hTrPCL30Xbi9-qHyqb2lAcI_FoFdk0HK" -O img2xml_weights.zip && rm -rf /tmp/cookies.txt



