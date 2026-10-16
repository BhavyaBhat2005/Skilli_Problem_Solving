def mostFrequent(nums):
    d = {}
    for i in nums:
        d[i] = d.get(i,0) + 1
    return sorted(d, key=lambda x: (-d[x], x))[0]