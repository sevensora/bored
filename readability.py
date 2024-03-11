from cs50 import get_string

text = get_string("Text: ")

sentence=0

letter=0

word=0

for x in text:
    if x.isalpha():
        letter += 1
    if x == " ":
        word += 1
    if x == "." or x == "?" or x == "!":
        sentence += 1
word += 1

letterword = letter / word *100

sentenceword = sentence / word *100

level = int((.0588 * letterword - .296 * sentenceword - 15.8)+.5)

if level < 1:
    print("Before Grade 1")
elif level >= 16:
    print("Grade 16+")
else:
    print(f"Grade {level}")

