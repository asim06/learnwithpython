import xlrd
import module1

#module1 tarafımca oluşturduğum, okunabilirliği attırması için fonksiyonlardan oluşan kütüphanedir.

#the library for read from excel file

#Read for Irregular Word LEARN GAME

def read_word_Irregular():
    path = "ListofIrregularVerbs.xlsx"
    inputWorkbook = xlrd.open_workbook(path)
    inputWorksheet = inputWorkbook.sheet_by_index(0)
    infinitive = []
    simple_past = []
    past_participle = []

    
    for y in range(inputWorksheet.nrows):

        infinitive.append(inputWorksheet.cell_value(y,0))
        simple_past.append(inputWorksheet.cell_value(y,1))
        past_participle.append(inputWorksheet.cell_value(y,2))
        
    return infinitive,simple_past,past_participle    
   

#Read for word LEARN GAME
def read_words():
    path = "worddatabase.xlsx"
    inputWorkbook = xlrd.open_workbook(path)
    inputWorksheet = inputWorkbook.sheet_by_index(0)

    words = []
    means = []
    synonym = []

    for y in range(inputWorksheet.nrows):
        words.append(inputWorksheet.cell_value(y,0))
        means.append(inputWorksheet.cell_value(y,1))
        synonym.append(inputWorksheet.cell_value(y,2))

    return words,means,synonym
    

def learn_word(words,means,synonym):
    wrong_answers = []
    #lenOfdata = 10
    count = 0
    say = 1
    #y = 0
    #end1 = 10
    y = int(input("please write start value for game \n :"))
    end1 = int(input("please write finish value for game \n :"))
    #for y in range(1,lenOfdata):
    while (y <= end1):


        if synonym[y] != 0:
            print("\t\t Reminder::::::: "+"Also there have synonym word in english you could check this word")
            print("\t\t",y,".Question: "+"What does of English word ?\t"+means[y]+"\t"+" Synonym mean: "+synonym[y])
            swap_mean = words[y]
            swap_mean_len = len(swap_mean)
            print("I have clue/hint for you "+swap_mean[0],(swap_mean_len-2)*" *",swap_mean[swap_mean_len-1])
            value = input("\n")

        else:
            #print("\t\t there havent synonym word in excel file")
            print("\t\t",y,".Question: "+"What does of English word ?\t"+means[y])
            swap_mean = words[y]
            swap_mean_len = len(swap_mean)
            print("I have clue/hint for you "+swap_mean[0],(swap_mean_len-2)*" *",swap_mean[swap_mean_len-1])
            value = input("\n")

           #check for answer
        if value == words[y]:
            print(10*"+"+"Correct"+"+"*10+"\n")
            
          
           
        else:

             print("\t\t\t\t\t***************Answer is not correct ***************")
             count += 1
             print("\t\t\t\t\t********** correct answer is :"+words[y]+"\n"+"\n")
             wrong_answers.append(y) 
             y = y - 1

        y = y +1 
            
         
    print("Sum of mistake",len(wrong_answers))
    
            
           
                   

def write_words(words,means,synonym):
    for i in range(1,10):
        print("\t"+words[i]+"\t\t"+"|"+means[i]+"|"+"\t"+str(synonym[i])+"\n")




infinitive,simple_past,past_participle = read_word_Irregular()
words,means,synonym = read_words()


print("\t Welcome to Game, We will learn new word or something, Good Luck \n")
print("\t There have two type game. They are names; ---learn Word and learn Irreguler Word---")
choose = input(" For learn, \n Word: 1 \n Irregular Word: 2 \n")
print("You're choosing",choose,"Game will start soon")
if choose == "1":
    choose1 = input("Do you want look all words before game ? you should write yes/no \n")
    if choose1 =="yes":
        write_words(words,means,synonym)
        learn_word(words,means,synonym)
    else:
        print("you're restirc")
        learn_word(words,means,synonym)

elif choose == "2":
    
    module1.gameMix(infinitive,simple_past,past_participle)
else:
    print("you've wrong chosen",choose)

    
