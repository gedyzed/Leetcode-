class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_words = {}
        answer = []

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_words:
                anagram_words[sorted_word].append(word)
            else:
                anagram_words[sorted_word] = [word]

        for value in anagram_words.values():
            answer.append(value)
        
        return answer

        