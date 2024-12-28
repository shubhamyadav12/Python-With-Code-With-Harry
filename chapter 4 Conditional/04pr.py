marks = 100

physics_marks = int(input("Enter your physics marks :"))
chemistry_marks = int(input("Enter your chemistry marks :"))
maths_marks = int(input("Enter your maths marks :"))

total_marks = physics_marks+chemistry_marks+maths_marks
percentage = (total_marks / 300) * 100

if physics_marks >= 33 :
  print("passesd in Physics")
else:
  print("you are failed in physics")  
if chemistry_marks >= 33 :
  print("passesd in chemistry")
else:
  print("you are failed in chemistry")  
if maths_marks >= 33 :
  print("passesd in maths")
else:
  print("you are failed in maths")  

if percentage >= 40 or physics_marks >= 33 and chemistry_marks>=33 and maths_marks>=33 :
 print("congratulation you are passes", percentage,"%")

else:
  print("Sorry you are failed") 