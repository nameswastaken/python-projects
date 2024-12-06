import random

var1 = random.randint(1, 20)
var2list = ["*", "/", "-", "+"]
var2 = random.choice(var2list)
var3 = random.randint(1,20)

print("You will be asked a random question. You must answer correctly, or you WILL be fail")
print(var1 + var2 + var3)