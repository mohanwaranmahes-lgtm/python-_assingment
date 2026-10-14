 if amount >= 1000 and membership == "yes":
        discount_percent = 20
    elif amount >= 1000:
        discount_percent = 10
    elif membership == "yes":
        discount_percent = 5
    else:
        discount_percent = 0
       discount = amount * discount_percent / 100
    final_amount = amount - discount
