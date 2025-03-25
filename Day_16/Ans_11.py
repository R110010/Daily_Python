# Create a function to find the most frequent word in a file.
count=0
my_dict ={}
def frequency(words):
    for word in words:
        if word in my_dict:
            my_dict[word]+=1
        else:
            my_dict[word]=1
    return my_dict
with open("my_text.txt","r") as file:
    data = (file.read()).split()
    resp =frequency(data)
    print(resp)
    