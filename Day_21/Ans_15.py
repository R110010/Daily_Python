# Find and return the longest word in a given list of words.
words = ["apple", "banana", "cherry", "dragonfruit", "elephant", "furniture", "grapefruits"]
longest_word = []
longest = 0
for word in words:
   if len(word)>longest:
      longest = len(word)
for word in words:
   if len(word)==longest:
      longest_word.append(word)
print("longest words : ",longest_word)