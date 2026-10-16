def secondHighestOccurringElement(nums):
    d = {}
    for x in nums:
        d[x] = d.get(x, 0) + 1
    f = sorted(set(d.values()), reverse=True)
    if len(f) < 2:
        return - 1
    return min(x for x in d if d[x] == f[1])