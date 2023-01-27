count = 0
while count <= 1:
    count = int(input("Введите количество чисел: "))

deystvie = input("Введите действие (+,-,/,*): ")

num1 = int(input("Введите 1 число: "))

for i in range(count - 1):
    num2 = int(input(f"Введите {i+2} число: "))
    if deystvie == "+":
        num1 += num2
    elif deystvie == "-":
        num1 -= num2
    elif deystvie == "/":
        if num1 == 0 or num2==0:
            print("Делить на ноль нельзя!")
            num1 = "Ошибка"
            break
        else:
            num1 /= num2
    elif deystvie == "*":
        num1 *= num2

print(f"Результат: {num1}")

