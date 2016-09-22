def get_string_dict(word) :
    d=dict()
    for c in word :
        d.setdefault(c,1)
        d[c]+=1
    keys=sorted(d)
    d1=dict()
    for k in keys :
        d1[k]=d[k]
    return d




s1=[]
with open('words.txt') as f :
    for line in f :
        s1.append(line.strip())
print get_string_dict(s1[0])
print get_string_dict(s1[1])
