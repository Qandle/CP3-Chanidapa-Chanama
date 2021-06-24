def login():
    username_input = input("Username : ")
    password_input = input("Password : ")
    if username_input == "admin" and password_input == "777":
        return True
    else:
        return False


def show_menu():
    print("------------------------------")
    print("Press 1 for Vat Calculator")
    print("Press 2 for Calculator")


def select_menu():
    print("------------------------------")
    press = input(">>")
    if press == "1":
        print("------------------------------")
        total_price = int(input("Price : "))
        print(vat_cal(total_price))
    elif press == "2":
        print("------------------------------")
        print(price_cal())
    else:
        print("Error!!")


def vat_cal(total_price):
    vat = 0.07
    price_add_vat = total_price * (1 + vat)
    return "Paid - " + str(price_add_vat) + " Baht"


def price_cal():
    price1 = int(input("1 st Price : "))
    price2 = int(input("2 nd Price : "))
    return vat_cal(price1 + price2)


if login():
    print("------------------------------")
    print("Welcome, admin.")
    show_menu()
    select_menu()
else:
    print("------------------------------")
    print("Wrong username or password!")  # แสดงกรณีพิมพ์ชื่อผู้ใช้หรือรหัสผ่านผิด
print("------------------------------")
