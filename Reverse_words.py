class Solution(object):
    def reverseWords(self, s):

       l=s.strip().split()
       res=''
       if len(l)==1 :
           return l[0]
       while len(l)!=0 :
          if len(l)!=1 :
           res+=l.pop()+' '
          else :
           res+=l.pop()
       return res
