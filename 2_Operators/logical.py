"""
Python has 3 logical operators
1. and
2. or
3. not

To check multiple condition
"""

"""
condition 1: purchase more than 1000 tk and
condition 2 : customer age less than 50 years and
condition 3 : if customer gender male will get "pen" and female will get "chocolate" as free and
condition 4 : payment on cash will get 10% discount , card will get 20% discount
"""

purchase = int(input("Purchase: "))
age = int(input("Age: "))
gander = input("Gender: ")
payment = input("Payment: ")

if purchase > 1000 and age < 50:
    print("Eligible for Discount")
    if gander == "male":
        print("Free Pen")
    elif gander == "female":
        print("Free Chocolate")
    if payment == "cash":
        print("After Discount 10% you have to pay")
        print(purchase - purchase * 10/100)
    elif payment == "card":
        print("After Discount 20% you have to pay")
        print(purchase - purchase * 20/100)
else:
    print("Not eligible for Discount")
