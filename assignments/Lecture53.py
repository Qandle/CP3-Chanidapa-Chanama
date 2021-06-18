def vat_cal(total_price):
    result = total_price * 1.07
    return result


price = int(input("Input price (Baht) : "))
print("Price include vat is", vat_cal(price), "Baht")
