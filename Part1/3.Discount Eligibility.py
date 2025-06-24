purchase_amount = 150
if purchase_amount > 100:
    print("You quality for a discount!")
    if purchase_amount >= 200:
        print("You get a premium discount!")
    else:
        print("You get a standard discount")
else:
    print("No discount avaliable.")