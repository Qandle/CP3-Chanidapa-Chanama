menuList = []
priceList = []
while True:
    menuName = input("Please Enter Menu :")
    if menuName.lower() == 'exit':
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
print(menuList, priceList)


def show_menu():
    print("------Receipt------")
    sum = 0
    for i in range(len(menuList)):
        print(menuList[i], priceList[i], "Baht")
        sum += int(priceList[i])
    print("total : %d Baht" % sum)


show_menu()
