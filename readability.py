from cs50 import get_string

text = get_string("Text: ")

sentence = letter = word = 0

for x in text:
    if x.isalpha():
        letters += 1
    elif x = "":
        word += 1
    elif x == "." or x == "?" or i == "!"
        sentence += 1

index = .0588 * (letter/word * 100) - .296 * (sentence/word * 100) - 15.8

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16)

