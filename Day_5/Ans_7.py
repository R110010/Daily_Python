# stop loop after 7 runs
i=1
limit=7
while (i<=10):
    print( i," loop")
    if i==limit:
        break
    else:
        i+=1
        continue