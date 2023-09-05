def afficher_message():
    print("ok")
    
    a = "premier"
    b = "second"
    
    return a,b
    
def deuxierme(a,b):
    
    print(a)
    print(b)  
    
def choixcalcul():
    
    choix = '4'
    
    match choix:
        case '1':
            result = addition(num1, num2)
        case '2':
            result = soustraction(num1, num2)
        case '3':
            result = multiplication(num1, num2)
        case '4':
            result = "r"
        case _:
            print("Choix invalide.")    
        
        case '3':
            result = multiplication(num1, num2)
        case '4':
            result = "r"
        case _:
            print("Choix invalide.")    
        case '3':
            result = multiplication(num1, num2)
        case '4':
            result = "r"
        case _:
            print("Choix invalide.")    
        
        
    print(result)
    
if __name__=="__main__":
    a,b = afficher_message()
    deuxierme(a,b)
    choixcalcul()