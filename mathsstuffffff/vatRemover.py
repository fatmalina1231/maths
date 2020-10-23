

print("Calculates original price based off current price and discount")

while True:
  print(" ")
  c = input("1 for add, 2 for subtract ")
  if (c == "1"):
    val = float(input("Current value? " ))
    per = float(input("Percentage added? " ))
    print(" ")
    print("Original price:")
    print((val/(per+100))*100)
    # THIS has given incorrect answers and I didn't notice until today. 2021/08/24
    
  elif (c == "2"):
    val = float(input("Current value? " ))
    per = float(input("Percentage off? " ))
    print(" ")
    print("Original price:")
    print(val * (1 + per/100))
    
  else:
    break
  
