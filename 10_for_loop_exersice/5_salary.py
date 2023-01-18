tabs = int(input())
contract_salary = int(input())


salary = contract_salary
for i in range(1, tabs + 1):
    site = input()
    if site == "Facebook":
        salary -= 150
    elif site == "Instagram":
        salary -= 100
    elif site == "Reddit":
        salary -= 50

    if salary < 0:
        break
if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)