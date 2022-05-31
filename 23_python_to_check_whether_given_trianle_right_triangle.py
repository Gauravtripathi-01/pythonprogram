side1=eval(input("Enter the first side of the triangle :  "))
side2=eval(input("Enter the second side of the triangle : "))
side3=eval(input("Enter the third side of the triangle : "))

if side1>=side2 and side1>=side3:
    largest_side= side1
elif side2>=side1 and side2>=side3:
    largest_side=side2
else:
    largest_side= side3
if largest_side==side1:
     if side1**2 == side2**2 + side3**2 :
        print("Given triangle is right triangle")
     else:
        print("Triangle is not right triangle")
if largest_side==side2:
     if side2**2 == side1**2 + side3**2 :
        print("Given triangle is right triangle")
     else:
        print("Triangle is not right triangle")
if largest_side==side3:
     if side3**2 == side1**2 + side2**2 :
        print("Given triangle is right triangle")
     else:
         print("Triangle is not right triangle")
else:
    print("Invalid input ")
