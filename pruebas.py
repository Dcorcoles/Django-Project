'''
x=0
while x<10:
    print("No aun no, x= " + str(x))
    x+=1

print("Ahora si, x= " + str(x))
'''
def intentos(n):
    x=1
    while x <= n:
        print("Intento " + str(x))
        x +=1
    print("Hecho")
    
intentos(5)
'''
username = get_username()
while not valid_username(username):
    print("Invalid username. Try again.")
    username = get_username()
'''
x = 1
sum = 0
while x < 10:
    sum += x
    x += 1
    
product = 1
while x < 10:
    product *= x
    x += 1
    
print(sum, product)

def count_down(start_number):
  current= start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)