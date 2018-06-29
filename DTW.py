# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 19:17:12 2018

@author: tinatsai
"""

import numpy as np

def DTW(obser,obser_):
    n = len(obser)
    m = len(obser_)
    DP = np.zeros((n,m))   #n*m的矩陣
    Dis = np.zeros((n,m))
    
    #生成原始距离矩阵
    for i in range(0,n,1):
        for j in range(0,m,1):
                Dis[i,j] = abs(obser_[j-1]-obser[i-1])
        
    #最短距離    
    for i in range(0,n,1):
            DP[i,0] += Dis[i,0]
    for i in range(0,n,1):
        for j in range(1,m,1):
            DP[0,j] += Dis[0,j]
    
    for i in range(1,n,1):
        for j in range(1,m,1):
            DP[i,j] +=min (min(DP[i-1,j-1],DP[i-1,j]),DP[i,j-1])+Dis[i,j] 
    return Dis, DP
