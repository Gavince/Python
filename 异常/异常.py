"""
python异常的语法:
try:
    尝试执行的代码
except:
    出现异常的处理情况

.异常1:
  .
  .
  .
  .
  .
.异常n:

else:
    #没有异常才能执行的代码
    pass

finally：
    #无论是否有异常都执行的代码
    pass

"""
print("-"*50)
try:
    num = int(input("Please enter a number:"))
    result = 8 / num

#有多少种异常 就列出来
except ZeroDivisionError: #针对某一个特殊的异常
    print("ZeroDivisionError！")
except ValueError:
    print("Please enter correct number!")
else:
    print("Try success！")
finally:
    print("Anyway!")

print("-"*50)