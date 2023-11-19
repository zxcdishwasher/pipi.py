import random
list = ["@","a","b","c","d","e","f","g","h","i","j","k","l","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]
a = int(input('какую длинну пароля вы бы хотели'))
pasword = ""
for i in range(a):
    b = random.choice(list)
    pasword += b
print(pasword)