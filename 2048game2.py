import random
import os

Rules = '''1. Same number will only add with same Numbers
2. After every 4 moves new Number will come
3. After every 2 moves it will ask to input the index to move another number
4. is at any block 512 number you made you won'''

controlers = '''
W for up
A for Left
S for Right
Z for Down'''

print("****128 game****")

lis = [2, 4, 8]
box = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]


def pbox():
    global box
    print()
    for i in box:
        print(i)
    print()


def keys(row, col):
    global box
    print(controlers)
    key = input("Enter the key : ").upper()
    try:
       if key == 'A': #Left
           if (box[row][col] == box[row][col-1]):
               box[row][col-1] = box[row][col] + box[row][col-1]
               box[row][col] = 0
           else:
              box[row][col], box[row][col-1] = box[row][col-1], box[row][col]
         
   
       elif key == 'S': #right
           if (box[row][col] == box[row][col+1]):
               box[row][col+1] = box[row][col] + box[row][col+1]
               box[row][col] = 0
           else:
              box[row][col], box[row][col+1] = box[row][col+1], box[row][col]
   
       elif key == 'Z':#down
           if (box[row][col] == box[row+1][col]):
               box[row+1][col] = box[row][col] + box[row+1][col]
               box[row][col] = 0
           else:
              box[row][col], box[row+1][col] = box[row+1][col], box[row][col]
       elif key == 'W': #up
           if (box[row][col] == box[row-1][col]):
               box[row-1][col] = box[row][col] + box[row-1][col]
               box[row][col] = 0
           else:
               box[row][col], box[row-1][col] = box[row-1][col], box[row][col]
       else:
          print("Invalid key!")
          pbox()
          keys(row, col)
          pass
       os.system('cls')
    except Exception as e:
       print()
       print(e)



count = 0
tobreck = False

while not tobreck:
   if count % 3 == 0:
     while True:
       Toadd = random.choice(lis)
       xyz = random.randint(0, 3)
       fRow = 0
       box[fRow][xyz] = Toadd
       break

   count+=1
   print(f"Your Number of steps : {count}")
   pbox()

   if count:
      while True:
        print("Which index you want to move? ")
        try:
           row = (int(input("Row(1-4) = ")) - 1)
           col = (int(input("Colum(1-4) = ")) - 1)
        except Exception as e:
           print(e)
           continue
        
        if (0 <= row and row < 4) or (0 <= col and col < 5):
           keys(row,col)
           break
        else:
          print("Worng Index !!")
          continue
             
   print()

   for i in box:
       if 128 in i:
           tobreck = True
           pass
       pass
   if tobreck:
       print("Congratulation!, You Won")
       
