def add(a, b):
  """Adds two numbers together."""
  return a + b

def subtract(a, b):
  """Subtracts one number from another."""
  return a - b

def multiply(a, b):
  """Multiplies two numbers together."""
  return a * b

def divide(a, b):
  """Divides one number by another."""
  if b == 0:
    return "Error: Cannot divide by zero"
  else:
    return a / b

while True:
  print("Select operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")

  choice = input("Enter choice(1/2/3/4/5): ")

  if choice in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Please enter numbers only.")
      continue

    if choice == '1':
      print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
      print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
      print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
      print(num1, "/", num2, "=", divide(num1, num2))
  elif choice == '5':
    break
  else:
    print("Invalid input. Please enter a valid choice.")
