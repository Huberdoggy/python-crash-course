"""Simple program that allows a user to continuously input numbers, appends to list
    and adds the total. Will check for non-digit input and skip as appropriate."""
import sys, math

result_lst = []
total = ''
while True:
    try:
        prompt = input("Enter a number: ")
        if prompt == 'q':
            break
        # elif isinstance(prompt, float):
        #     prompt = float(prompt)
        #     result_lst.append(prompt)
        else:
            prompt = int(prompt)
            result_lst.append(prompt)
    except ValueError:
        pass

if len(result_lst) > 0:
    for number in result_lst:
        if len(result_lst) == 1:
            total = number
            print(f"Total: {total}")
        elif len(result_lst) > 1:
            total = math.fsum(result_lst)
    print(f"The sum of all number you provided me today is: {total}")
else:
    print("No calculation needed..good-bye")
    sys.exit()

