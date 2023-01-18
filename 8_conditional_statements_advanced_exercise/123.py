if operator in ['+', '-', '*']:
    print(f"{n1} {operator} {n2} = {income} - {even_or_odd})"
if operator == '/':
    print(f"{n1} '/' {n2} = {income:.2f}")
elif operator == '%':
    print(f"{n1} % {n2} = {income}")
elif n1 == 0:
    print(f"Cannot divide {n2} by zero")
elif n2 == 0:
    print(f"Cannot divide {n1} by zero")