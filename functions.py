
def verif_num():
    valid = False
    while not valid:
        print("Digite um valor:")
        try:
            x = float(input())
        except ValueError:
            print("Valor inválido")
        else:
            valid = True

    
    return x
