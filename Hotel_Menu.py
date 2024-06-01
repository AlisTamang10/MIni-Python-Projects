print("--------------- Hamro Restro Menu ----------------")
menu = {
    "Pizza" : 250,
    "Mo:Mo" : 120,
    "Chowmin" : 100,
    "Coffee": 80,
    "Cold drinks": 80
}
for i,j in menu.items():
    print(i,":",j)
print("-----------------------------------------------------")    
order_total = 0
order_items= []
while True:
    item = input("Enter the name of item you want to order:")
    if item in menu:
        order_total = order_total + menu[item]
        order_items.append(item)
        print(f"{item} has been added to your order list.")
    else:
        print(f"Currently {item} is not available on our menu.")
        
    second_order = input("Do you like to place another order.(Yes/No): ")
    
    if second_order == 'No':
        break
    
print("----------------Here is the bill sir ! ---------------")
for order_item in order_items:
    print(f"{order_item} : Rs.{menu[order_item]}")
    
print(f"Your total amount is {order_total}")
print("Thank you for visiting us")