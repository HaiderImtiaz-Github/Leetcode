class Solution(object):
    def countConsistentStrings(self, allowed, words):
        self.char = set(allowed) 
        self.number_output = 0  
        print(f"Output: {self.check_words(words)}")

    def check_words(self, words):
        for word in words:
            if set(word).issubset(self.char):  
                self.number_output += 1  
        return self.number_output
    
my_soln = Solution()
allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
    
my_soln.countConsistentStrings(allowed, words)
