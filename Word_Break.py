
class Solution(object):


    def __init__(self) :

        self.dp=dict()


    def isWordBreaking(self,word) :

        if len(word)==0 : return True

        if word in self.dp :
            return self.dp[word]

        if len(word)==1 :
            return False


        for i in range(1,len(word)) :

            left=word[0:i]
            right=word[i:]

            l,r=False,False

            if left not in self.dp :
                self.dp[left]=self.isWordBreaking(left)

            l=self.dp[left]

            if right not in self.dp :
                self.dp[right]=self.isWordBreaking(right)

            r=self.dp[right]

            if l and r :
                return True


        return False






    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """


        for word in wordDict :
            self.dp[word]=True

        return self.isWordBreaking(s)




        
