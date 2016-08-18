a=[10, 90, 49, 2, 1, 5, 23]


def kth_largest_number(low,high,k) :

    if low>high :
        return -1

    pivot=a[low]
    l=low+1
    r=high


    while l<r :

        if pivot>a[l] :
            temp=a[l]
            a[l]=a[r]
            a[r]=temp
            r-=1
        else :
           temp=a[l]
           a[l]=a[l-1]
           a[l-1]=temp
           l+=1

    if (l-1)==k :
        return a[l-1]

    if (l-1)> k :
        return partition(low,l-1)

    return partition(l,high)


print "aa"
print kth_largest_number(0,len(a)-1,2)
print a
