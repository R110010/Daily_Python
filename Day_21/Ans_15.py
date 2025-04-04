# Find and return the longest word in a given list of words.
words = ["apple", "banana", "cherry", "dragonfruit", "elephant", "furniture", "grapefruits"]
longest = ""
for word in words:
   if len(word)> len(longest):
      longest = word
print(" longest word ",longest)