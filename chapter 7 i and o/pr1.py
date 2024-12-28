with open("poems.txt") as f:
    content = f.read()
    if ("twinkle" in content):
        print("twinkle word is present in poem line")
    else:
        print("twinkle word is not present in poem line") 