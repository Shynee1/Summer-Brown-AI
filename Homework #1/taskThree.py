def get_length(text):
    chars = 0
    for i in range(len(text)):
        chars += 1
    return chars

text = input("Enter text: ")
print("# of Characters: " + str(get_length(text)))