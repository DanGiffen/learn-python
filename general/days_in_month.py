#calc

#add
def add(n1, n2):
  """Take 2 integers as input and return the addition"""
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide (n1, n2):
  return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# -- my solution. works but is more code-- 

# if operation_symbol == "+":
#   answer = add(num1, num2)
# elif operation_symbol == "-":
#   answer = subtract(num1, num2)
# elif operation_symbol == "*":
#   answer = multiply(num1, num2)
# elif operation_symbol == "/":
#   answer = divide(num1, num2)

calculation_finished = False
num1 = int(input("What's the first number?: "))

for symbol in operations:
  print(symbol)
operation_symbol = input("Choose an operation from the list above: ")

while not calculation_finished:
  num2 = int(input("What's the next number?: "))
  calculation_function = operations[operation_symbol]
  # gets the value of the symbol key
  answer = calculation_function(num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  continue_calc = input(f"Type y to continue calc with {answer}, or type n to exit.: ").lower()
  if continue_calc == "y":
    num1 = answer
    operation_symbol = input("Select an operation: ")
    num2 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  else:
    calculation_finished = True
    
  


