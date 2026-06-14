class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            anagram_basic = str(sorted(word))
            if anagram_basic in hashmap: hashmap[anagram_basic].append(word)
            else: hashmap[anagram_basic]=[word]
        return [hashmap[el] for el in hashmap]