# input statements
salary = float(input("Enter the employee's salary: "))
numDependents = float(input("Enter the number of dependents: "))

# calculate taxes here
stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = salary * 0.025 * numDependents
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding
# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
print("stateTax: $" + str(salary * 0.065))
print("federalTax: $" + str(salary * 0.28))
print("dependentDeduction: $" + str(salary * 0.025 * numDependents))