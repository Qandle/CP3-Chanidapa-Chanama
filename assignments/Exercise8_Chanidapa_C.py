usernameKey = "admin"
passwordKey = "password"
usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == usernameKey and passwordInput == passwordKey:
    print("----------------------Amazing Cafe---------------------")
    print("   Welcome", usernameKey, "!")
    print("--------------------------Menu-------------------------")
    print("1 - Mocha                 50 Baht")
    print("2 - Americano             45 Baht")
    print("3 - Cappuccino            65 Baht")
    print("4 - Chocolate             45 Baht")
    print("5 - Milk tea              70 Baht")
    print("------------------------------------------------------ ")
    selectMenu = input("Would you like to drink some coffee? (menu no.) \n press number : ")  # เลือกเมนู
    cups = int(input("How many cups do you want? \n press number : "))  # เลือกจำนวนแก้ว
    if cups >= 0:
        print("------------------------------------------------------ ")
        if selectMenu == "1":
            print("Price >>", 50 * cups, "Baht")
        elif selectMenu == "2":
            print("Price >>", 45 * cups, "Baht")
        elif selectMenu == "3":
            print("Price >>", 65 * cups, "Baht")
        elif selectMenu == "4":
            print("Price >>", 45 * cups, "Baht")
        elif selectMenu == "5":
            print("Price >>", 70 * cups, "Baht")
        else:
            print("Sorry, I could not get what you choose.")  # แสดงกรณีเลือกเมนูไม่ถูกต้อง
    else:
        print("Sorry, I could not get how many you choose.")  # แสดงกรณีเลือกเมนูไม่ถูกต้อง
else:
    print("------------------------------------------------------ ")
    print("Wrong username or password!")  # แสดงกรณีพิมพ์ชื่อผู้ใช้หรือรหัสผ่านผิด
print("------------------------------------------------------ ")

