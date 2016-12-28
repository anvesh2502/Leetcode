def getParanthesesCombinations(n,s='') :

    if n==1 : return '()'

    if len(s)==2 : return '()'

    s='()'*n

    res=s[2:]

    perms=getParanthesesCombinations(n,res)

    i=0
    output=set()

    for p in perms :

        j=0
        while j<=len(p) :
            output.add(p[0:j]+'()'+p[j])
            j+=1


    return output

print getParanthesesCombinations(3)            
