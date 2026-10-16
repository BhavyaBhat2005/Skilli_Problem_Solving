def sumOfFrequencies(arr):
    d = {}
    for x in arr:
        d[x] = d.get(x,0) +1
    return max(d.values()) + min(d.values())