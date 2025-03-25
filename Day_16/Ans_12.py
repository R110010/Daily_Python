# Find the longest word in a text file.
with open("my_text.txt","r")as file:
    words = (file.read()).split()
    longest= len(words[0])
    for word in words:
        if len(word)>=longest:
            longest = len(word)
            longest_word = word
        else:
            continue
    print(" the longest word is ",longest_word)