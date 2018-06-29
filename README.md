# Implementation-of-Dynamic-Time-Warping-DTW-
Speech recognition Spring 2018, NYUST

Using DTW on the MFCC's to match a spoken word to a template

1. Use MFCC to analysis audio's features
2. Use DTW to find the shortest path

# The topic of DTW
• If the audio which we want to compare have different length(vector), we use DTW to find the distance between them. 
![alt tag](http://mirlab.org/jang/books/dcpr/example/output/dtwBridgePlot03.png)

# The principle of DTW
There are three parts of DTW:

## - Recurrence Relation 遞迴關係

## - Tabular Computation 列表式運算

## - Traceback 路徑回朔

• Determin D(i , j) = Distance between ti, rj;

• A(i, j) = the shortest cumulative distance value (begin point(1, 1) to end point (i, j))

• Use Reccurence Relation to find the shortest cumulative distance value between vector(t) and vector(r)

## Sum A(N,M)，Formula:
## A(i, j) = D(i, j) + min{A(i - 1, j), A(i - 1, j - 1), A(i, j - 1)}

![alt tag](https://i.imgur.com/XkC1An3.png)
