
# # Define the spam keywords
# spam_keywords = ["Make a lot of money", "buy now", "subscribe this", "click this"]

# # Input the comment
# comment = input("Enter the comment: ")

# # Check if the comment is spam
# is_spam = False
# for keyword in spam_keywords:
#     if keyword.lower() in comment.lower():
#         is_spam = True
#         break

# # Output the result
# if is_spam:
#     print("This is a spam comment.")
# else:
#     print("This is not a spam comment.")




    # second method

p1 = "follow this"
p2 = "subscribe this"
p3 = "join this"
p4 = "buy this"

messege = input("type here your comment : ")

if ((p1 in messege) or (p2 in messege) or (p3 in messege) or (p4 in messege)):
    print("this is a spam comment")

else:
   print("this is not a spam comment")

