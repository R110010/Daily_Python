# Use filter() to find words longer than 5 characters.
words =["appy","lucky","juniper","dhuppi","pumpkin","tar","gum"]
res = list(filter(lambda x:len(x)>=5,words))
print(res)    