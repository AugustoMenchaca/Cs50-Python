import os
os.system('cls')
import sys
from pizza import verificar
import csv
def main():
    if len(sys.argv) ==1 or len(sys.argv)==2:
        print("Too few arguments in line")
    elif len(sys.argv)>=4:
        sys.exit("Too many arguments in line")
    elif len(sys.argv)==3:
        arquivo=sys.argv[1]
        new_arquivo=sys.argv[2]
        if verificar(arquivo):
            try:
                with open(arquivo,'r')as file:
                    reader=csv.reader(file)
                    next(reader,None)
                    with open(new_arquivo,'w',newline="")as new_file:
                     writer=csv.writer(new_file)
                     for row in reader:
                            name = row[0].strip('"')
                            house = row[1]
                            try:
                                last,first = name.split(",")
                                writer.writerow([first.strip(), last.strip(), house.strip()])
                            except:
                                print(f"Couldn't split name: {name}")                       
            except Exception as e:
                sys.exit(f"Error {e}")
        else :
            print("Invalid file")
if __name__=="__main__":
    main()

        