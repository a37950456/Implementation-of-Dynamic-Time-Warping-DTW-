#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:48:47 2018

@author: tinatsai
"""
#!/usr/bin/env Python
# coding=utf-8
#import numpy as np
import librosa  as lb
from scipy.io import wavfile
import DSPbox as dsp
import DTW as DTW_Tina

import time

    
if __name__ == '__main__':
    fs, sig = wavfile.read('Observation.wav','r')
    obser = dsp.MFCC(sig,fs)
    #print(obser)

    file = ['1.wav', '2.wav', '3.wav', '4.wav', '5.wav']
    Distance = []

    tStart = time.time()#計時開始
    for index in file:
        fs, sig = wavfile.read(index ,'r') 
        obser_ = dsp.MFCC(sig,fs)
        D, wp =lb.dtw(obser, obser_)# Obervation與 wav1 都是音訊檔的MFCC特徵向量#D是路徑迴溯矩陣
        #print('Wp=',wp)
        #print('D=',D)
        A = (D[D.shape[0]-1 ,D.shape[1]-1]) #最後的累積距離值A(N,M)
        print(index,'.wav A(N,M)=',A,sep='')
        Distance.append(A)
        #print (Distance)
    
    count =1
    for index in Distance:
        ++count
        if index == min(Distance):
            print ('Ans = ',count,'.wav', sep='')
            
    tEnd = time.time()
    print ("DTW by python cost %f sec" % (tEnd - tStart))#會自動做近位

    tStart_ = time.time()#計時開始
    for index in file:
        fs, sig = wavfile.read(index ,'r') 
        obser_ = dsp.MFCC(sig,fs)
        #print('obser_=',obser_)
        #print('obser=',obser)
        Dis, DP = DTW_Tina.DTW(obser, obser_)# Obervation與 wav1 都是音訊檔的MFCC特徵向量#D是路徑迴溯矩陣
        #print ('Dis=',Dis)
        #print ('DP=',DP)
        A = (DP[DP.shape[0]-1 ,DP.shape[1]-1])
        print(index,'.wav A(N,M) =',A,sep='')
        Distance.append(A)
        #print (Distance)
    
    count =1 
    for index in Distance:
        ++count
        if index == min(Distance):
            print ('Ans = ',count,'.wav', sep='')

    tEnd_ = time.time()
    print ("DTW by Tina cost %f sec" % (tEnd_ - tStart_))#會自動做近位