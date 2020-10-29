import xlrd
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


def gamev1(infinitive,simple_past,past_participle):
    print("Game is starting \n")
    y = 0
    lenofData = 10
    wrong_answer = []
    
    while (y <= lenofData):
        print("What is correct v1 word ?"+"\t"+simple_past[y]+"\t"+past_participle[y]+"\n")
        
        value =input("")
        if value == infinitive[y]:
            print("You're answer correct :)")
        else:
            print("You're not answer correct :("+"\t"+infinitive[y]+"\t"+simple_past[y]+"\t"+past_participle[y]+"\n")
            wrong_answer.append = y

        y = y + 1

infinitive,simple_past,past_participle =  read_word_Irregular()

print(infinitive)

print("Welcome new game, you will learn Irregular Word"+"What do you learn ?"+"v1,v2,v3")

choose = input("just chose one , \n v1 \n v2 \n v3 \n mix \n")

if choose == "v1":
    print("You will learn v1")
    gamev1(infinitive,simple_past,past_participle)
   

elif choose== "v2":
    print("You will learn v2")

elif choose == "v3":
    print("You will learn v3")

elif choose == "mix":

    print("You will learn mix word type")
else:
    print("wrong choose ! be carefull just chose one , \n v1 \n v2 \n v3 \n")

lenofData = len(infinitive)
