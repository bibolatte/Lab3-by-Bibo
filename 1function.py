def my_function():
  print("Hello from a function")
my_function()

#3
def my_function1(fname, lname):
  print(fname)

#4
def my_function2(x):
  return x + 5

#5
def my_function(*kids):
  print("The youngest child is " + kids[2])

#6
def my_function(**kid):
  print("His last name is " + kid["lname"])