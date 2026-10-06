while True:
  a = int(input("enter first nu1mber: "))
  b = int(input("enter second number: "))
  c = input("enter a sign: ")

  if c == "+":
    print(a + b)
  elif c == "-":
    print(a - b)
  elif c == "*":
    print(a * b)
  elif c == "/":
    if b == 0:
      print("error")
    else:
      print(a / b)
  elif c == "//":
    if b == 0:
      print("error")
    else:
      print(a // b)
  elif c == "**":
    print(a**b)
  elif c == "%":
    if b == 0:
      print("error")
    else:
      print(a % b)
  else:
    print("error")
    