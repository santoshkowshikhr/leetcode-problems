class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set(\qwertyuiop\)
        set2 = set(\asdfghjkl\)
        set3 = set(\zxcvbnm\)
        result = []


        for word in words:
            low_words = set(word.lower())

            if low_words <= set1 or low_words <= set2 or low_words <= set3:
                result.append(word) 

        return result
        