from employee import Employee

first_name = input("What's your first name? => ")
last_name = input("And how about your last name? => ")
current_salary = int(input("Finally, your current annual salary? => "))
add_salary = Employee(first_name, last_name, current_salary)

print(
    "We will now prompt to increase your salary."
    " Enter 'q' at any time to quit. Or, enter 'd' for the default value"
    " of $5,000\n"
)
while True:
    response = input("Amount? [amount/d/q] => ")
    if response == "q":
        break
    elif response == "d":
        current_salary = add_salary.give_raise()
    else:
        current_salary = add_salary.give_raise(response)

# Show the new salary
print(
    f"Annual salary for {first_name.title()} {last_name.title()} is: {current_salary:,}"
)
