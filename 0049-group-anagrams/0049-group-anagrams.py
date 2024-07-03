class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_words = defaultdict(list)
  
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_words[sorted_word].append(word)
        
        return anagram_words.values()

        