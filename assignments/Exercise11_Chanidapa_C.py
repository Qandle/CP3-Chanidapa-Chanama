# การสร้างเป็นพีระมิดที่สามารถกำหนดความสูงได้จาก input
x = int(input("Input number : "))
a = x
for j in range(x):
    for i in range(a-1):
        print(" ", end="")  # show space before *
    a -= 1
    print("*"*(j*2+1))  # show *
