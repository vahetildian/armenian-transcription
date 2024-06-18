def listToStr(aList:list)->str:
    aString=""
    for element in aList:
        aString+=element
    return aString

def armToStr(someInput:str)->str:
    """Returns a string; Dont forget to use it, with print() for instance"""
    dictOfSounds={"Ա":"A","Բ":"B","Գ":"G","Դ":"D","Ե":"È","Զ":"Z","Է":"É","Ը":"ET","Թ":"T","Ժ":"J","Ի":"I","Լ":"L","Խ":"KH","Ծ":"TS","Կ":"K","Հ":"H","Ձ":"DZ","Ղ":"R","Ճ":"TSH","Մ":"M","Յ":"I","Ն":"N","Շ":"SH","Ո":"(V)O","Չ":"TCH","Պ":"P","Ջ":"DJ","Ռ":"R","Ս":"S","Վ":"V","Տ":"T","Ր":"R","Ց":"TS","Ւ":"U","Ու":"OU","Փ":"P","Ք":"K","Օ":"O","Ֆ":"F","և":"IEV","ա":"a","բ":"b","գ":"g","դ":"d","ե":"è","զ":"z","է":"é","ը":"et","թ":"t","ժ":"j","ի":"i","լ":"l","խ":"kh","ծ":"ts_","կ":"k","հ":"h","ձ":"dz","ղ":"r","ճ":"tsh","մ":"m","յ":"i","ն":"n","շ":"sh","ո":"(v)o","չ":"tch","պ":"p","ջ":"dj","ռ":"r","ս":"s","վ":"v","տ":"t","ր":"r","ց":"ts_","ւ":"u","ու":"ou","փ":"p","ք":"k","օ":"o","ֆ":"f","և":"iev"}

    result=[]
    for letter in someInput:
        if letter in dictOfSounds:
            result.append(dictOfSounds[letter])
        else:
            result.append(letter)


    #you can already print the result here, but it's not perfect
    #listToStr(result) #before transforming the vo


    #Starting here: transforming the (v)o in "vo" or "o" depending on context

    #for debugging:
    #print("")
    #print("#transforming the (v)o in \"vo\" or \"o\" depending on context")
    #print("")


    if result[0]=="(V)O":
        result[0]="Vo"

    index=1
    length=len(result)
    while index <length:
        if result[index]=="(V)O":
            if result[index-1]==" ":
                result[index]="Vo"
            else:
                result[index]="o"

        elif result[index]=="(v)o":
            if result[index-1]==" ":
                result[index]="vo"
            else:
                result[index]="o"

        index+=1

    #print(result) #for debugging
    return(listToStr(result))

if __name__=="__main__":
    userInput=input()
    print(armToStr(userInput))
