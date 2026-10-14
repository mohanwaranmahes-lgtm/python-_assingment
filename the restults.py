 print("Original amount:", amount)
    print("Discount percentage:", discount_percent, "%")
    print("Discount amount:", discount)
    print("Final payable amount:", final_amount)

    if discount_percent > 0:
        print("Eligibility status: Eligible for discount")
    else:
        print("Eligibility status: Not eligible for discount")
else:
    print("Invalid membership status. Enter yes or no.")
