price=int(input("enter your price:"))
percent_discount=int(input("enter percent discount:"))
discount=price*percent_discount/100
total_price=price-discount
print("original price",price)
print("Discount Amount",discount)
print("Discounted price",total_price)