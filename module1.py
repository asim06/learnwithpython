import xlrd
import random
   

def gamev1(infinitive,simple_past,past_participle):
    print("Game is starting \n")
    print("There have",len(infinitive),"word")
    print("How many do you want learn word ? "+"You should write start and end of values")
    start_value = int(input(":"))
    end_value = int(input(":"))
    #y = 0
    y = start_value
    #lenofData = 10
    wrong_answer = []
    
    while (y <= end_value):
        print(y,".Question "+"What is correct v1 word ?"+"\t \t"+simple_past[y]+"\t"+past_participle[y]+"\n")
        
        value =input("")
        if value == infinitive[y]:
            print("You're answer correct :) \n")
        else:
            print(y,".Question "+"You're not answer correct :("+"\t"+infinitive[y]+"\t"+simple_past[y]+"\t"+past_participle[y]+"\n")
            wrong_answer.append(y)
            y = y - 1

        y = y + 1




def gameMix(infinitive,simple_past,past_participle):
    print("Game is starting . . . .  . .  . .  . . .  . . . .  . . . . . .  . . . . . . .  \n")
    print("There have",len(infinitive),"word \n")
   
    v1_game = 0
    v2_game = 1
    v3_game = 2
    y = 0
    check = 1
    #rand_game = 0
    while (y <= 10):
        if check == 1:
             rand_game = random.randint(0,2)

        
        if rand_game == v1_game:
            
            print(y,".Question "+"What is correct v1 word: "+"\t"+" \t?"+"\t"+simple_past[y]+"\t"+past_participle[y]+"\n")
            value =input("")
            if value == infinitive[y]:
                 print("You're answer correct :) \n")
                 check = 1
                 
            else:
                 print(y,".Question "+"---------- You have written wrong answer ----------"+"\t"+infinitive[y]+"\t"+simple_past[y]+"\t"+past_participle[y]+"\n")
                 y = y - 1
                 check = 0
                
        
        elif rand_game == v2_game:
             print("Random game is creating, you will play v2 game")
             print(y,".Question "+"What is correct v2 word: "+"\t \t"+infinitive[y]+"\t"+"\t ?"+"\t"+past_participle[y]+"\n")
             value =input("")
             if value == simple_past[y]:
                 print("You're answer correct :) \n")
                 check = 1
                 
             else:
                 print(y,".Question "+"---------- You have written wrong answer ----------"+"\t"+infinitive[y]+"\t"+simple_past[y]+"\t"+past_participle[y]+"\n")
                 y = y - 1
                 check = 0

           
        elif rand_game == v3_game:

            print("Random game is creating, you will play v3 game v")
            print(y,".Question "+"What is correct v3 word: "+"\t \t"+infinitive[y]+"\t"+"\t"+simple_past[y]+"\t "+"\t?"+"\n")
            value =input("")
            if value == past_participle[y]:
                print("You're answer correct :) \n")
                check = 1
                 
            else:
                 print(y,".Question "+"---------- You have written wrong answer ----------"+"\t"+infinitive[y]+"\t"+simple_past[y]+"\t"+past_participle[y]+"\n")
                 y = y - 1
                 check = 0


        y = y + 1


   

    


