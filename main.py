#Write your code below this line 👇
import math
def paint_calc(height, width, cover): 
    area = height * width
    number_of_cans = math.ceil(area/cover)
    print(f"You will need {number_of_cans} number of cans")
 #Inputs after defining
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
    








    




