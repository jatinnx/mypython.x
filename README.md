import time
import random


print("****************************************************")
print("\tWELLCOME TO THE ONE PIECE QUIZ GAME")
print("****************************************************")
numQue = 0
score = 0
emty = []
print("Let's start the Game in", end = ' ', flush = True)

for i in range(3, 0, -1):
    print(i, end=' ', flush=True)
    time.sleep(1)  # Add a delay of 1 second between each number

print("Go!")

quebank = { 
    "What is the name of Luffy's ship after the Going Merry?" : 
    ["1) Thousand Sunny" , "2) Grand Line Explorer", "3) Blackbeard's Revenge", "4) Straw Hat Marauder"],

    "Which character is known for using a three-sword style in combat?" : 
    ["1) Usopp","2) Sanji","3) Zoro","4) Nami"],

    "What is Nami's primary goal throughout the series?" : 
    ["1) To become the strongest swordsman", "2) To find the legendary treasure, One Piece", "3) To draw a complete map of the world","4) To become the Pirate King"],

    "Who is the archaeologist and historian in the Straw Hat Pirates crew?": 
    ["1) Franky","2) Nico Robin","3) Brook","4) Chopper"],

    "What is Sanji's dream in the series?":
    ["1) To find the All Blue", "2) To become the world's greatest swordsman","3) To map the entire world","4) To become the Pirate King"],
    
    "Which Devil Fruit ability does Luffy possess?": 
    ["1) Gomu Gomu no Mi (Rubber-Rubber Fruit)" , "2) Mera Mera no Mi (Flame-Flame Fruit)","3) Hana Hana no Mi (Flower-Flower Fruit)","4) Gura Gura no Mi (Tremor-Tremor Fruit)" ],
    
    "Who is the reindeer doctor in the Straw Hat Pirates crew?":
    ["1) Sanji","2) Usopp","3) Chopper","4) Zoro"],
    
    "What is Zoro's ultimate goal in the series?":
    ["1) To find the legendary treasure, One Piece", "2) To become the world's greatest swordsman", "3) To become the Pirate King", "4) To uncover the true history of the world" ],
    
    "Which character is a living skeleton musician?":
    ["1) Franky", "2) Jinbe", "3) Brook","4) Nami"],
    
    "What is the name of the island where the Straw Hat Pirates found Tony Tony Chopper?":
    ["1) Drum Island", "2) Water 7",  "3) Alabasta","4) Enies Lobby"]

    }

ansbank = [ "1) Thousand Sunny","3) Zoro","3) To draw a complete map of the world","2) Nico Robin","1) To find the All Blue","1) Gomu Gomu no Mi (Rubber-Rubber Fruit)", "3) Chopper", "2) To become the world's greatest swordsman", "3) Brook","1) Drum Island" ]

quelist = list(quebank.keys())

def answer(que, anss):
    global numQue, score
    numQue += 1
    qindx = quelist.index(que)
    if anss == ansbank[qindx] :
        score += 1
        print("Congratulations!!, You Gave the Right Answer")
        print(f"Your score is {score} out of {numQue}")
    else:
        print("It a worng Answer")
        print(f"Right Answer Is [{ansbank[qindx]}]")
        print(f"Your score is {score} out of {numQue}")
    pass

end = False
while not end:
    i = random.choice(quelist)
    # print(emty)
    if (emty.count(i)):
        continue
    emty.append(i)

    time.sleep(0.38)
    print(i)
    time.sleep(0.38)
    print(quebank[i][0])
    time.sleep(0.38)
    print(quebank[i][1])
    time.sleep(0.38)
    print(quebank[i][2])
    time.sleep(0.38)
    print(quebank[i][3])
    time.sleep(0.38)

    ans = int(input("Enter your Answer (1/2/3/4) : "))
    ansStr = quebank[i][ans - 1]
    

    answer(i, ansStr)
