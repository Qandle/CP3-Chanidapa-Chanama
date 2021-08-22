menuList = []
while True:
    menuName = input("Please Enter Menu :")
    if menuName.lower() == 'exit':
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName, menuPrice])


def show_menu():
    print("------Receipt------")
    sum = 0
    for i in range(len(menuList)):
        for j in range(len(menuList)):
            print(menuList[i][j], end=' ')
        print('Baht')
        sum += int(menuList[i][1])
    print("total : %d Baht" % sum)


show_menu()
