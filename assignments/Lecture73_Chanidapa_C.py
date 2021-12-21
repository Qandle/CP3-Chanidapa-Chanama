menuList = []
menuBar = {'menu1': 20,
           'menu2': 30,
           'menu3': 60}
while True:
    menuName = input("Please Enter Menu :")
    if menuName.lower() == 'exit':
        break
    else:
        menuPrice = menuBar[menuName]
        menuList.append([menuName, menuPrice])
print(menuList)


def show_menu():
    print("------Receipt------")
    sum = 0
    for i in range(len(menuList)):
        for j in range(2):
            print(menuList[i][j], end=' ')
        print('Baht')
        sum += int(menuList[i][1])
    print("total : %d Baht" % sum)


show_menu()
