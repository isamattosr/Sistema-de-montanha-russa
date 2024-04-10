def sistema_de_montanha_russa (idade_da_pessoa, altura_da_pessoa):  
    if idade_da_pessoa <10 and altura_da_pessoa <1.60:
        print ("voce nao pode embarcar na monatanha russa")
    elif idade_da_pessoa >=10 and altura_da_pessoa >=1.65:
        print ("voce pode embarcar na montanha russa.")

while True:
    idade_da_pessoa = int (input("digite a sua idade: "))
    altura_da_pessoa = float (input("digite a sua altura: "))
    sistema_de_montanha_russa (idade_da_pessoa, altura_da_pessoa)

    encerrar = str (input("digite sair se quiser encerrar: "))
    if encerrar == "sair":
        print ("fim")
        break