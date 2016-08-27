class Solution(object):
    def wordPattern(self, pattern, s):

       l=s.split()
       d=dict()
       i=0
       keys=set()

       if len(pattern)!=len(l) : return False


       while i<len(pattern)  :

           c=pattern[i]
           word=l[i]

           print c,word

           if c not in d :
               if word in keys :
                   return False
               d[c]=word
           else :
               if d[c]!=word : return False
           keys.add(word)
           i+=1

       return True
