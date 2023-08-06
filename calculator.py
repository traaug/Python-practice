def calculator(express):
    return eval(express)  # eval function calculate what in the string


user_express = input("enter the operation: ")
while user_express != "off":
    if '^' in user_express:
        user_express = user_express.replace('^', '**')
    print(calculator(user_express))
    user_express = input("enter the operation: ")
