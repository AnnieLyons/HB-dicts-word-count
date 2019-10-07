# put your code here.

words = {}
log_file = open("test.txt")


for line in log_file:
    line.rstrip()
    word_list = line.split(" ")
    word_list = tuple(word_list)
    # print(word_list)
    
    for word in word_list:
        words[word] = words.get(word_list, 0) + 1

print(words)


# print(words)
