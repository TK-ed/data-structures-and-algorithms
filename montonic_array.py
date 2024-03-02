def monotonic_array(array):
    if array is None:
        return True
    first = array[0]
    last = array[len(array)-1]
    # 1 2 3 4 1
    if first == last:
        for i in range(0, len(array)-1):
            if array[i] != array[i+1]:
                return False
    # 10 9 8 7 6
    elif first > last:
        for i in range(0, len(array)-1):
            if array[i+1] > array[i]:
                return False
    #  1 2 3 4 5
    else:
        for i in range(0, len(array)-1):
            if array[i+1] < array[i]:
                return False
    return True
arr = []
n = int(input())
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
monotonic_array(arr)