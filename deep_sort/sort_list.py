# -*- coding:utf-8 -*-
import os
txt_dir="/home/liuyp/liu/mot/deep_sort/demo/img2/det/det.txt"
new_dir="/home/liuyp/liu/mot/deep_sort/demo/img2/det/det_result.txt"
fl=open(txt_dir)
fl_a=fl.readlines()
fl_b=sorted(fl_a)
fl.close()
fl=open(new_dir,"w")
fl.close()
fl=open(new_dir,"r+")
for i in fl_b:
  fl.write(i+"\n")
print "over"
