# Find and return the longest word in a given list of words.
words = ["apple", "banana", "cherry", "dragonfruit", "elephant", "furniture", "grapefruits"]
max_length = max(len(word) for word in words)
longest = list(word for word in words if len(word)==max_length)
print(longest)