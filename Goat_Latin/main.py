class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = ["a", "e", "i", "o" ,"u"]
        spl = sentence.split()
        for i in range(len(spl)):
            if (spl[i][0] in vowel):
                spl[i] = spl[i] + "m" + ("a" * (i+2))
            else:
                spl[i] = spl[i][1:] + spl[i][0] + "m" + ("a" * (i+2))
        
        return (" ".join(spl))
                