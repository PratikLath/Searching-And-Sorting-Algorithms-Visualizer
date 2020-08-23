import time

def binary_search(data, search, drawData, timeTick):
    color=[]
    for i in range(len(data)):
        color.append('red')
    l=0
    r=len(data) - 1
    while l <= r: 
        mid = l + (r - l) // 2; 
        if data[mid] == search: 
            color[mid]='green' 
            drawData(data, color)
            time.sleep(timeTick)
            break
        elif data[mid] < search:
            for p in range(mid+1):
                color[p]='blue'
            drawData(data, color)
            time.sleep(timeTick)
            l = mid + 1
        else:
            for p in range(mid,len(data)):
                color[p]='blue'
            drawData(data, color)
            time.sleep(timeTick)
            r = mid - 1
        