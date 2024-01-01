# Exceptions: Try/Except and Raise
print('Errors: Try/Except')
try:
    num = int(input('Enter a number between 1 and 30: '))
    # print("30 divided by", num, "is:", 30/num) -> we comment it because it's written double but we still need its calculation
    num1 = 30/num
    if num > 30:
        raise ValueError(num)
except ZeroDivisionError as err:
    print(err, "==> You can't divide by Zero!!!")
except ValueError as err:
    print(err, num, "==> Bad Value not between 1 and 30!")
except:
    print("Invalid Input!")
else: # this program will start running if everything works well
    print("30 divided by", num, "is:", 30/num)
finally:
    print("**Thank you for playing!**")

#try:
    #code you want to run
#except:
    #executed if error occurs
#else:
    #executed if no error
#finally:
    #always executed
