class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded_word = str(len(word))+'#'+word
            encoded+="".join(encoded_word)
        return encoded
    def decode(self, s: str) -> List[str]:
        start_num_i, i=0, 0
        decoded=[]
        while(i<len(s)):
            if s[i]=='#':
                # length of the upcoming word
                length_word=int(s[start_num_i:i])
                decoded.append(s[i+1 : i+1+length_word])
                start_num_i = i+1+length_word
                i=start_num_i
            else: i+=1
        return decoded