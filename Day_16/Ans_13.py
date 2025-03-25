# Sort words in a file alphabetically and save the result.
def sort_words(input_file,output_file):
    with open(input_file,"r") as file:
        words = (file.read()).split()
        words.sort()
    with open(output_file,"w") as f:
        f.write("\n".join(words))

sort_words("input.txt","output.txt")