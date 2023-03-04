def mergesort(arr, l, r):

    #print('start: ', arr[l:r])

    if len(arr[l:r]) <=1:
        return arr[l:r]

    mid = l + (r-l) // 2
    left    = mergesort(arr, l, mid)
    right   = mergesort(arr, mid, r)
    # concatenate the left and right results into arr
    arr = left + right

    # realign the indexes with the new arr
    mid -= l
    r -= l
    l_idx = 0
    r_idx = mid
    final = []

    while l_idx < mid and r_idx < r:
        if arr[l_idx] <= arr[r_idx]:
            final.append(arr[l_idx])
            l_idx+=1
        else:
            final.append(arr[r_idx])
            r_idx+=1


    for val in arr[l_idx:mid]:
        final.append(val)

    for val in arr[r_idx:r]:
        final.append(val)

    return final

