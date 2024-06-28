import os 
os.system('cls')
import sys
from tabulate import tabulate
import csv
def main():
    if len(sys.argv) == 2:
        arquivo=sys.argv[1]
        if verificar(arquivo):
         try:
            with open(arquivo,'r')as file:
               reader=csv.reader(file)
               headers=next(reader)
               table=list(reader)
            print(tabulate(table, headers, tablefmt="grid"))
         except Exception as e:
            print(f"Error{e}")
    elif len(sys.argv)==1:
       print("Too few arguments for command")
    else :
       print("Too many arguments for command")
    

def verificar(arquivo):
    return os.path.isfile(arquivo)
if __name__=="__main__":
  main()

