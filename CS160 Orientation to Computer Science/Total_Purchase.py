# Total Purchase Exercise by Brady Esplin

item1 = float(input("Item 1 cost is?"))
item2 = float(input("Item 2 cost is?"))
item3 = float(input("Item 3 cost is?"))
item4 = float(input("Item 4 cost is?"))
item5 = float(input("Item 5 cost is?"))

subTotal = item1+item2+item3+item4+item5
salesTax = 0.07
taxPrice = subTotal*salesTax
grandTotal = subTotal+taxPrice


print("Subtotal is $")
print (format(subTotal, ".2f"))
print("The sales tax rate is 7%")
print("Tax is $")
print (format(taxPrice, ".2f"))
print("Your total price today is $")
print (format(grandTotal, ".2f"))



