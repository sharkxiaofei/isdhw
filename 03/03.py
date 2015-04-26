def binary_search(data,find,low=0,high=None):
    high = high if high is not None else len(data)
    while low < high:
        mid = (low + high) / 2
        midval = data[mid]
        if midval < find:
            low = mid + 1
        elif midval > find:
            high = mid
        else:
            return mid
    return - 1
