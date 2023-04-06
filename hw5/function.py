import collections
s = input("Write your sentence here:")

def most_common_letter():
    try:
        count=0
        new_letter = ""
        new_s = s.replace(" ", "")
        if len(new_s)<1:
            print("There are no words.")
        else:
            while count<3:
                new_letter=collections.Counter(new_s).most_common(1)[0]
                (letter, num) = new_letter

                print(collections.Counter(new_s).most_common(1)[0])
                new_s = new_s.replace(letter, "")
                count+=1
    except:
        if count<3:
            print("Sentence has less than three unique letters")
most_common_letter()
