weeks = ['S','M','T','W','T','F','S']

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

day31 = [1,3,5,7,8,10,12]
day30 = [4,6,9,11]
s = 'Year 2024'
month = int(input("Enter the month Number : "))
print("\t",s.center(20, '*'))
print("\t\t", months[month-1],"\n")
# a = 0
for j in weeks:
    print(j,"\t", end='')
print()

class printMonth:
     a = 8
     def Days31(self,month):
        a = 0
        if month == 1 or month == 7:
           print("-\t", end='')
           a +=1
        elif month == 3:
           for i in range(0,5):
            print('-\t', end='')
            a +=1
        elif month == 5:
           for i in range(0,3):
            print('-\t', end='')
            a +=1
        elif month == 8:
           for i in range(0,4):
            print('-\t', end='')
            a +=1
        elif month == 10:
           for i in range(0,2):
            print('-\t', end='')
            a +=1
        elif month == 12:
          pass
         
        for i in range(1, 32):
          print(i,'\t', end='')
          a+=1
          if a % 7 ==0:
             print()
     
     def Day29(self,month):
        a = 0
        for i in range(0,4):
           print('-\t', end='')
           a +=1
        for i in range(1, 30):
          print(i,'\t', end='')
          a+=1
          if a % 7 ==0:
             print()
        pass
     
     def Days30(self,month):
         a = 0
         if month == 4:
           print("-\t", end='')
           a +=1
         elif month == 6:
            for _ in range(0,6):
             print("-\t", end='')
             a+=1  
         elif month == 11:
            for _ in range(0,5):
             print("-\t", end='')
             a+=1  
         elif month == 9:
            pass  
            
         for i in range(1, 31):
          print(i,'\t', end='')
          a+=1
          if a % 7 ==0:
             print()
            
d = printMonth()
if(day31.count(month)):
   d.Days31(month)
elif(day30.count(month)):
   d.Days30(month)
elif month == 2:
   d.Day29(month)
   pass

def Note(date):
   f = open("Note", "a+")
   f.write(f"{date}/{month}/2024 :\n{input("Write your note:")} \n\n")
   pass

print("\n",d.a)
# ask = input("\n\nDo You want to make some note (yes or no) : ")
# if ask == 'yes':
#    date = input("Enter the Date (DD) : ")
#    Note(date)
#    pass
   
  
    


