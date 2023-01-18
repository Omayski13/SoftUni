n1 = int(input())
n2 = int(input())
operator = input()

even_or_odd = ''
income = 0

if operator == '+':
    income = n1 + n2
elif operator == '-':
    income = n1 - n2
elif operator == '*':
    income = n1 * n2
elif operator == '/':
    if n1 != 0 and n2 != 0:
        income = n1 / n2
elif operator == '%':
    if n1 != 0 and n2 != 0:
        income = n1 % n2

if operator in ['+','-','*']:
    if income % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'


if operator in ['+', '-', '*']:
    print(f"{n1} {operator} {n2} = {income} - {even_or_odd}")
elif operator == '/':
    if n1 == 0:
        print(f"Cannot divide {n2} by zero")
    elif n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} / {n2} = {income:.2f}")
elif operator == '%':
    if n1 == 0:
        print(f"Cannot divide {n2} by zero")
    elif n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} % {n2} = {income}")