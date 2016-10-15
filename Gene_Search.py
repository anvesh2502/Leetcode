
def greater(s1,s2) :

    i=0
    j=0

    while i<len(s1) and j<len(s2) :
        if ord(s1[i])>ord(s2[j]) : return True
        elif ord(s1[i])<ord(s2[j]) : return False
        i+=1
        j+=1

    return False


def compare(s1,s2) :

    i=0
    j=0

    if len(s1)==0 and len(s2)==0 : return True
    if len(s1)==0 or len(s2)==0 : return False



    while i<len(s1) and j<len(s2) :
        if s1[i]!=s2[j] :
            return False
        i+=1
        j+=1

    return True

def get_suffix_array(s) :

   d=dict()

   for i in range(0,len(s)) :
       d[i]=s[i:]

   return sorted(d,key=d.get)


def g_search(gene,pattern,suffix_array,low,high) :

 if low>high : return False

 mid=(low+high)/2
 sub=text[suffix_array[mid]:]
 if compare(sub,pattern) :
     return True
 elif not greater(patter,sub) :
     return find_pattern(gene,pattern,suffix_array,low,mid-1)
 return find_pattern(gene,pattern,suffix_array,mid+1,high)


def gene_search(gene,pattern) :

    suffix_array=get_suffix_array(gene)

    return g_search(gene,pattern,suffix_array,0,len(suffix_array)-1)









print gene_search("ACCATGCA", "CAT") # => True
print gene_search("CATTGA", "CAT") # => True
print gene_search("GGCACACATG", "CACAT") # => True
print gene_search("CAAAT", "CAT") # => False
