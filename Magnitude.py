from math import *
fraction = ["/", "d", "c", "m", "/", "/", "µ", "/" , "/", "n", "/", "/", "p", "f", "/", "/", "a",]
multiple = ["/", "da", "h", "k", "/", "/", "M", "/", "/", "G", "/", "/", "T", "/", "/", "P", "/", "/", "E", "/", "/", "Z", "/", "/", "Y"]
main = ["m", "g", "s", "l"]

file = open("README.txt", "r")

for line in file:
  print(line)
  
value = float(input("Enter value: "))
type = input("Enter type: ")
magnitude = input("Enter magnitude: ")
result_type = input("Enter resultvalue: ")

if multiple.count(type) >= 1: # calculate power to go back main
  value = value * pow(10, multiple.index(type))
elif fraction.count(type) >= 1:
  value = value * pow(10, -(fraction.index(type)))
print("In main value: " + str(value))

if multiple.count(result_type) >= 1: # calculate result power
  value = value * pow(10, -(multiple.index(result_type)))
elif fraction.count(result_type) >= 1:
  value = value * pow(10, fraction.index(result_type))
  
print("result: " + str(value))