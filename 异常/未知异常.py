try:
    num = int(input("Please enter a number:"))
    result = 8 / num
    print(result)

except ValueError:
    print("Please enter correct number!")
except Exception as result:#未知错误的捕获
    print("未知错误 %s" % result)

print("-"*50)
