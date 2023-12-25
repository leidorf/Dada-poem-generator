import random
words_per_line = int(input("Enter the number of words per line: "))
text_input = input("Please enter a text to create a dada poem.\n")
words = text_input.split()
random.shuffle(words)

lines = [words[i:i+words_per_line] for i in range(0, len(words), words_per_line)]
print("Lines:")
for line in lines:
    print(' '.join(line))