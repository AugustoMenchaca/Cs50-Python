import os 
os.system('cls')
import sys
def verificar(pasta, nome_arquivo):
    caminho = os.path.join(pasta,nome_arquivo)
    return os.path.isfile(caminho), caminho
def contar(caminho):
    with open(caminho, 'r')as arquivo:
        linhas = arquivo.readline()
        return len(linhas)
def main():
    nome_arquivo = sys.argv[1]
    pasta= sys.argv[2]
    arquivo_existente, caminho = verificar(pasta, nome_arquivo)
    if arquivo_existente:
        linhas=contar(caminho)
        print({pasta},{linhas})
    else :
        print("Não tem esse arquivo")
    
if __name__=="__main__":
    main()

       
    