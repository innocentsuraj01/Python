r = int(input("Enter number of row:"))
for i in range (0, r):
   for j in range (0, r-i+1):
      print (end=" ")
   for j in range (0, i):
      print ("*", end ="")
   print()

for i in range (r, 0,-1):
   for j in range (0, r-i+1):
      print (end=" ")
   for j in range (0, i):
      print ("*", end ="")
   print()

