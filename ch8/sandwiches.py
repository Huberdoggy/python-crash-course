from functions import make_sandwich

# ALTERNATIVELY, TO IMPORT A FUNCTION AS AN ALIAS TO AVOID NAMING CONFLICTS, USE THE 'AS' SYNTAX:
# EX. from 'module_name' import 'make_sandwich as 'alias_name'
# You can also ALIAS the MODULE itself, as in: import 'module_name' as 'alias_name'
# Import EVERY function from a module, using the asterisk wildcard: Ex. from 'module_name' import * - not good practice


bread_type = 'wheat'
complete_order_list = []
add_these = []

print("Follow the instruction prompts to build your sandwich.")
while True:
    i_name = input("What stuff do you want on your sandwich (Or 'q' to quit now) => ")
    if i_name == 'q' and len(add_these) == 0:
        break
    elif i_name == 'q' and len(add_these) > 0:
        finished_sandwich = make_sandwich(bread_type, add_these)
        print(f"Here's your customized sandwich:\n\t{finished_sandwich}")
        complete_order_list.append(finished_sandwich)
        add_these = []
    else:
        add_these.append(i_name)
        if len(add_these) >= 3:
            ask = input("Still want to add more? (y/n) => ")
            if ask == 'y':
                pass
            else:
                finished_sandwich = make_sandwich(bread_type, add_these)
                print(f"Here's your customized sandwich:\n\t{finished_sandwich}")
                complete_order_list.append(finished_sandwich)
                add_these = []
                if len(complete_order_list) >= 1:
                    print("Lets make another!!")
                    print(f"Now starting on sandwich {len(complete_order_list) + 1}")

print('-' * 70)
print(f"\nAnd here's all the stored sandwich data from today's input:\n\n\t*****SANDWICHES FROM TODAY*****")
for made_sandwich in complete_order_list:
    print(f"\n\t{made_sandwich}")
