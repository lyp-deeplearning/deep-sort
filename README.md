# deep-sort
tracking by deep learning
- detecor:SSD512 
- association:Deep-sort  
you can get the [paper](https://arxiv.org/pdf/1703.07402.pdf) here  
This demo refers to [SSD](https://github.com/SpyderXu/ssd_sort) and [deep-sort](https://github.com/nwojke/deep_sort/issues/68)

## Result
![image](https://github.com/lyp-deeplearning/deep-sort/blob/master/deep_sort/result/aa.png)
## Introduction
If you want to use this demo ,you should install [SSD](https://github.com/weiliu89/caffe/tree/ssd) .Also,there is a pretrained SSD model offerd to you. When you use this model generate the pedestrain detection result , this result needs being saved as txt format.Fianlly, you can use your test data with the Deep-sort method .  
## Dependencies
The code is compatible with Python 2.7 and 3. The following dependencies are needed to run the tracker:
- NumPy
- sklearn
- OpenCV
- TensorFlow (>= 1.0)
- Caffe
## Contents
tips: if you just want to test the deep-sort method with the MOT datasets, you can follow this [link](https://github.com/lyp-deeplearning/deep-sort/tree/master/deep_sort) to operate your code. This page is telling you how to use your own dataset completing MOT.  
1、 generate the detection result  
You can use your own detector ,and also we will provide a detector here. The result will be saved as a txt according the MOT format:

```
the line of txt :
10,-1,171,239,136,361,0.9933876,-1,-1,-1
frame ID,-1,XMIN,YMIN,width,height,confidence,-1,-1,-1
```
This part can follow another projiect here.
2、generate feature vectort information
According to the deep-sort paper,the distance which caculetes with kalman filter predicting and detector is using the feature vector. This feature vector is extracting with a CNN network.Please put your testing data in demo file folder,the output_dir is a separate binary file in NumPy native format which storing the feature information

```
python tools/generate_detections.py --mot_dir=./demo/ --output_dir=demo_output/ --model=resources/networks/mars-small128.pb
```
3、


