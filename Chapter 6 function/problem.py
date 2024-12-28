def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
          n.append(item.strip(word))
    return n    

l = ["harry", "shubham", "rohan", "hanuman", "ranjan"]

print(rem(l, "an"))
