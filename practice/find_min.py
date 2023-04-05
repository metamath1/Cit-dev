from typing import Union

def min(L: list) -> Union[int,float]: 
    v = L[0]

    for i in L[1:]:
        if i < v:
            v = i
    
    return v

print( min([4.4, 156, 11, 45, 31, 98]) )
