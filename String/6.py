# Find the length of the longest word in a string
s="this is yet another string for testing."
s_words = s.split()
print(s_words)
longest_word = ""
longest= 0
for word in s_words:
    count=0
    for char in word:
        count+=1
    if count > longest:
        longest = count
        longest_word = word

print(longest,longest_word)