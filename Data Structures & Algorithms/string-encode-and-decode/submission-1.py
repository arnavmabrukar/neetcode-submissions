class Solution:

    def encode(self, strs: List[str]) -> str:
        newString=""
        for word in strs:
            length = str(len(word))
            newString = newString + (length+"#"+word)
        return newString

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != '#': #need a while loop
                j += 1
            # once we find delim
            length = int(s[i:j]) # i to j gives the num; change to int
            start = j+1 # end of delim; start of word
            end = start + length # where the word starts + the length of the word
            decoded.append(s[start:end])
            i = end # fix the inf loop; update jump
        return decoded