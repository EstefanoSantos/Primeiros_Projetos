import os

lista = []

while True:
    print('Selecione uma opcção.')
    entrada = input("[i]nserir  [a]pagar  [l]istar: ")

    if entrada == 'i' or 'I':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif entrada == 'a' or 'A':
        indice_str = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um inteiro.')
        except IndexError:
            print('Valor não existe no indice.') 
        except Exception:
            print('Erro desconhecido.')           
    elif entrada == 'l' or "L":
        if len(lista) == 0:
            print('Não existe nada na lista.')
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Insira i, a ou l.')            
        
