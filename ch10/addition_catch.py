"""PROMPT A USER FOR 2 NUMBERS. ADD THEM TOGETHER
AND CATCH ERROR IF THEY ARE NOT DIGIT VALUES (WILL BE OF TYPE STR ON INITIAL INPUT,
BUT THE PURPOSE HERE IS TO CHECK IF THE 'STR' ITSELF IS A DIGIT)"""


def add_numbers(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return num1 + num2


def check_is_digit(input_str):
    if input_str.strip().isnumeric():
        return True
    else:
        return False


first_num = input("Enter a number => ")
second_num = input("Enter another number and I will add them up => ")

if check_is_digit(first_num) and check_is_digit(second_num):
    print(f"Adding {first_num} + {second_num}...")
    result = add_numbers(first_num, second_num)
    print(f"Result is: {result}")
elif not check_is_digit(first_num):
    print(f"{first_num} is NOT a valid integer digit")
elif not check_is_digit(second_num):
    print(f"{second_num} is NOT a valid integer digit")
else:
    pass
