import time 
import logging
# import bankd
import os

bankName = ("""
***********************************************
           WELCOME TO YOUR BANK
***********************************************

""")


mainMenu = ("""
1. Creat Bank Account
2. Withdraw Money
3. Diposite Money
4. Check Balence 
5. Exit
""")


def Transaction(name, money , vari):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(name)
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    if vari == 1:
      logger.info(f"Rupees {money} has been Deposited in your Bank Account")
    elif vari == 2:
      logger.info(f"Rupees {money} has been Withdraw from your Bank Account")

def Balence2(bhName):
    with open(bhName, "r+") as bankFile :
        fristLine = bankFile.readline()
        balence = fristLine.split(':')
        xc = balence[1]
    return int(xc)

class BankOP:   
    def accountManeger(self,bhName,Money, passw):
        with open(bhName, "a+") as bankFile :
            bankFile.write(f"Balence : {Money} \n")
            bankFile.write(f"Password : {passw} \n")
        Menu()
        pass

    def checkpass(self, bhName, pin):
          with open(bhName, "r+") as bankFile :
            pL = bankFile.readlines()
            password = pL[1].split(':')
            correct = int(password[1]) 
          return True if (pin == correct) else False
               
    def Balence(self, bhName):
        with open(bhName, "r+") as bankFile :
          fristLine = bankFile.readline()
          balence = fristLine.split(':')
          xc = balence[1]
          print(f"Balence : {xc} \n")
          sec = 5
          while sec > 0:
            print(f"Logging out in {sec} sec", end= '\r')
            time.sleep(1)
            sec -= 1

          os.system('cls')    
          Menu()
        pass
    
A = BankOP()

class AccountManeger:
    def Diposite(self, bhName, Money):#, Date):
        with open(bhName, "r+") as bankFile :
            fristLine = bankFile.readline()
            balence = fristLine.split(':')
            un = int(balence[1])
            bankFile.seek(len("Balence : "))
            bankFile.write(f"{un + Money}")
        Transaction(bhName,Money,1)
        
        A.Balence(bhName)
        pass

    def Withdraw(self, bhName, Money):
        isThere = Balence2(bhName)
        if isThere < Money:
          print(f"Blance : {isThere} ")
          print("You Don't have minimun Amount\n\n")
          sec = 5
          while sec > 0:
            print(f"Logging out in {sec} sec", end= '\r')
            time.sleep(1)
            sec -= 1
            os.system('cls')
            Menu()
        
        with open(bhName, "r+") as bankFile :
            fristLine = bankFile.readline()
            balence = fristLine.split(':')
            un = int(balence[1])
            bankFile.seek(len("Balence : "))
            # bankFile.write(f"{un - Money}")
        with open(bhName, "r+") as bankFile :
            f1 = bankFile.read()
            replce = f1.replace(balence[1], f" {un - Money}\n") 

        with open(bhName, "w") as bankFile :
            bankFile.write(replce)
        
        Transaction(bhName, Money, 2)

        A.Balence(bhName)
    pass

class Bank:
    def __init__(self, bankHolderName):
        self.bankHolder = bankHolderName
        print("Account has beed created")
        self.balence = 0
        print(f"Your Account balence is {self.balence}")
        pass
    def Diposite(self , addmoney, passw):
        self.balence += addmoney
        print("Your Amount has been Diposite, SUCCESSFULLY !!")
        print(f"Your Account balence is {self.balence}")
        A.accountManeger(self.bankHolder, self.balence, passw)

        pass

def Oparetion(options):
    if options != 5:
       name = input("Enter your Account name here : ")
       nameLog = name + ".log"
    #    password = input("Enter you PassWord : ")

    if (options == 1):
        with open(nameLog, "w") as bankFile :
            pass
        
        holder = Bank(nameLog)
        dipositeMoney = int(input("Enter your amount to Diposite : "))
        password = input("Enter your Password : ")
        holder.Diposite(dipositeMoney, password)
        pass
    elif (options == 2):
        a = False
        while not a:
            password = int(input("Enter you PassWord : "))
            right = A.checkpass(nameLog , password)
            if(right):
                holde = AccountManeger()
                amount = int(input("Enter your Amount to Withdraw : "))
                holde.Withdraw(nameLog, amount)
                a = True
            else:
                print("Password is incorrect")
                pass
        pass
    elif (options == 3):
        a = False
        while not a:
            password = int(input("Enter you PassWord : "))
            right = A.checkpass(nameLog , password)
            if(right):
                a = True
                holder = AccountManeger()
                amount = int(input("Enter your Amount to Diposite : "))
                holder.Diposite(nameLog, amount)
            else:
                print("Password is incorrect")
                pass
        pass  
    elif (options == 4):
        a = False
        while not a:
            password = int(input("Enter you PassWord : "))
            right = A.checkpass(nameLog , password)
            if(right):
                a = True
                A.Balence(nameLog)
            else:
                print("Password is incorrect")
                pass
        
        pass   
    elif (options == 5):
        print("Thank you ")
        exit()

def Menu():
     print(bankName)
     time.sleep(0.25)
     print(mainMenu)
     options = int(input("How can I help you (enter the num accordingly) :  "))
     time.sleep(0.5)
     Oparetion(options)

if __name__ == "__main__":
    Menu()