import collections
s = "Write a function that takes in a sentence and returns the 3 most common letters."
new_s=s.replace(" ", "")
print(collections.Counter(new_s).most_common(1)[0])