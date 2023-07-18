#####################################################################
# 실습문제38: 표준편차 구하기
# lab 38
import math

L = [1,2,3,4,5,6,7,8,9,10]

def mean(L):
    return sum(L) / len(L)

def std(L):
    sigma = 0.0

    m =  sum(L) / len(L)
    dev = [ (l - m)**2 for l in L ]
    # sigma = math.sqrt( sum(dev) / (len(dev)-1) )
    sigma = math.sqrt(mean(dev))
    
    return sigma
        

print(mean(L), std(L))
##################################################################### 