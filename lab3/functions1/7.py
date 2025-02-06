def has_33(num):
    for i in range(len(num)):
        if num[i] == 3:
            if num[i - 1] == 3 or num[i + 1] == 3:
                return True
            return False


num = list(input("Enter the array: "))
print(has_33(num))

