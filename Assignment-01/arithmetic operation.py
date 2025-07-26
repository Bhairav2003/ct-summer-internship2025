a_input = input()
b_input = input()

if (a_input.lstrip('-').isdigit() and b_input.lstrip('-').isdigit()):
    a = int(a_input)
    b = int(b_input)
    
    # Perform operations
    print(a + b)   
    print(a - b)   
    print(a * b)   
else:
    print("Invalid input. Please enter integer values.")
