# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 09:09:28 2020

@author: Aniket Maity
"""




def main():
    N,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    
    sum = 0
    aCount = x
    bCount = y
    for i in range(5):
        if(a[i]>=b[i] and aCount>0):
            aCount -=1
            sum+=a[i]
        elif(b[i]>=a[i] and bCount>0):
            bCount -=1
            sum+=b[i]
            
    print(sum)

if __name__== '__main__':
    main()
        
        