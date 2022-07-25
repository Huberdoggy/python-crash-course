import sys

print("Give me two numbers, and I'll divide them." " (or enter 'q' to quit)")

while True:
    first_num = input(f"\nFirst number? => ")
    if first_num == "q":
        break
    second_num = input("Second number? => ")
    if second_num == "q":
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print(f"Cant perform zero-division on {first_num}")
        sys.exit(1)
    else:
        print(answer)
