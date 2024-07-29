import math
def sockmerchant(n, ar):
    color_count={}
    pairs=0

    for color in ar:
        if color in color_count:
            color_count[color]+=1
        else:
            color_count[color]=1

    for count in color_count.values():
        pairs +=count// 2
    return pairs

n=9
ar=[10,20,20,10,10,30,50,10,20]

print(sockmerchant(n, ar))