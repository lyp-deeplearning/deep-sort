# deep-sort
tracking by deep learning
- detecor:SSD512 
- association:Deep-sort  
you can get the [paper](https://arxiv.org/pdf/1703.07402.pdf) here  
This demo refers to [SSD](https://github.com/SpyderXu/ssd_sort) and [deep-sort](https://github.com/nwojke/deep_sort/issues/68)

## Result

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
This part can follow another project here.  

2、generate feature vectort information
According to the deep-sort paper,the distance which caculetes with kalman filter predicting and detector is using the feature vector. This feature vector is extracting with a CNN network.Please put your testing data in demo file folder,the output_dir is a separate binary file in NumPy native format which storing the feature information

```
python tools/generate_detections.py --mot_dir=./demo/ --output_dir=demo_output/ --model=resources/networks/mars-small128.pb
```

3、runing the traker
In this part ,you can run the deep_sort_app.py to generate the result:

```
python deep_sort_app.py  --sequence_dir=./demo/img2/  --detection_file=./demo_output/img2.npy --min_confidence=0.5 --nn_budget=200 --display=True --output_file=result/a.txt
```

4、generate the video
If you want your data merging into a video, you can run code as follow:

```
python generate_videos.py --mot_dir=demo/img2/img1/ --result_dir=result/ --output_dir=/home/liuyp/liu/mot/deep_sort/videos/
```

5、testing MOT dataset
If you want to test the MOT dataset, you should run this code:

```
python evaluate_motchallenge.py --mot_dir=test/ --detection_dir=./resources/detections/MOT16_POI_test/ --min_confidence=0.4

```
## Citing deep-sort
If you find this repo useful in your research, please consider citing the following papers:

```
@inproceedings{Wojke2017simple,
  title={Simple Online and Realtime Tracking with a Deep Association Metric},
  author={Wojke, Nicolai and Bewley, Alex and Paulus, Dietrich},
  booktitle={2017 IEEE International Conference on Image Processing (ICIP)},
  year={2017},
  pages={3645--3649},
  organization={IEEE},
  doi={10.1109/ICIP.2017.8296962}
}

@inproceedings{Wojke2018deep,
  title={Deep Cosine Metric Learning for Person Re-identification},
  author={Wojke, Nicolai and Bewley, Alex},
  booktitle={2018 IEEE Winter Conference on Applications of Computer Vision (WACV)},
  year={2018},
  pages={748--756},
  organization={IEEE},
  doi={10.1109/WACV.2018.00087}
}
```
Finally, if you have any question about this project, you can contact me by my email .

