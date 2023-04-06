import collections
s = "Write a function that takes in a sentence and returns the 3 most common letters."

def most_common_letter():
    new_letter = ""
    new_s = s.replace(" ", "")
    for i in range(3):
        new_letter=collections.Counter(new_s).most_common(1)[0]
        (letter, num) = new_letter

        print(collections.Counter(new_s).most_common(1)[0])
        new_s = new_s.replace(letter, "")
most_common_letter()