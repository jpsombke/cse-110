# I added a prompt for the user to enter how many child soft drinks & how many adult soft drinks are ordered and the corresponding price for those two. 
child_price_num = float(input("What is the price of a child's meal? "))
adult_price_num = float(input("What is the price of an adult's meal? "))
child_num = int(input("How many children are there? "))
adult_num = int(input("How many adults are there? "))

child_soft_drink_price = float(input("What is the price of a child soft drink? "))  # Convert to float
adult_soft_drink_price = float(input("What is the price of an adult soft drink? "))  # Convert to float
child_soft_drink_num = int(input("How many child soft drinks? "))
adult_soft_drink_num = int(input("How many adult soft drinks? "))

subtotal_num = (child_price_num * child_num) + (adult_price_num * adult_num) + (child_soft_drink_num * child_soft_drink_price) + (adult_soft_drink_num * adult_soft_drink_price)
formatted_subtotal = "${:.2f}".format(subtotal_num)

print("Subtotal:", formatted_subtotal)

sales_tax_rate = float(input("What is the sales tax rate? "))  
sales_tax_num = subtotal_num * (sales_tax_rate / 100)  

formatted_sales_tax = "${:.2f}".format(sales_tax_num) 
print("Sales Tax:", formatted_sales_tax)

total_num = subtotal_num + sales_tax_num 
formatted_total = "${:.2f}".format(total_num)
print("Total:", formatted_total)

payment_amount_num = float(input("What is the payment amount? "))
change_num = payment_amount_num - total_num
formatted_change_num = "${:.2f}".format(change_num)
print("Change:", formatted_change_num)








