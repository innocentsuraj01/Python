n = int(input("Eneter a number:"))
num = n
Result = 0
while n > 0: 
    digit = n % 10
    n = n // 10
    Result = Result + digit
print ("sum of digit of", num ,"is", Result)