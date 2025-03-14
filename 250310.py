class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = {v: 0 for v in vowels}
        consonants = 0
        left = 0
        valid_substrings = 0
        distinct_vowels = 0
        
        for right in range(len(word)):
            if word[right] in vowels:
                if vowel_count[word[right]] == 0:
                    distinct_vowels += 1
                vowel_count[word[right]] += 1
            else:
                consonants += 1
            
            while left <= right and (consonants > k or distinct_vowels < 5):
                if word[left] in vowels:
                    vowel_count[word[left]] -= 1
                    if vowel_count[word[left]] == 0:
                        distinct_vowels -= 1
                else:
                    consonants -= 1
                left += 1
            
            if distinct_vowels == 5 and consonants == k:
                valid_substrings += (left + 1)
        
        return valid_substrings