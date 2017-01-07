
def get_magic_index(l,low,high) :

    if low>high :
        return -1

    if low==high :

        if l[low]==low : return low
        return -1

    mid=(low+high)/2

    if a[mid]==mid :
        return mid

    if a[mid]>mid :
        return get_magic_index(l,mid+1,high)

    return get_magic_index(l,low,mid-1)

l=[-1,0,1,2,4,10]

print get_magic_index(l,0,len(l)-1)
