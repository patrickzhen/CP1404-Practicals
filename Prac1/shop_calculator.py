

Total_money = 0
Number_of_items = int(input("Number of items: "))
if Number_of_items > 0:
    for i in range(Number_of_items):
        prices = float(input("Item Price: "))
        Total_money += prices
    print("Original Price: ", Total_money)

else:
        print("You don't have anything in the cart") #check section

if Total_money > 100:
    print("You pay: ", Total_money*0.9) #discount section











