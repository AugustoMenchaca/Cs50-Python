import os, re 
os.system('cls')
def main ():
    v1=input("Ipv4: ")
    validate(v1)
    if validate(v1)==True:
        print("Valid")
    else:
        print("Invalid")
def validate(v1):
    match=re.match(r"([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})",v1,re.IGNORECASE)
    try:
        if int(match.group(1))<=255 and int(match.group(2))<=255 and int(match.group(3))<=255 and int(match.group(4))<=255:
            return True
    except AttributeError:
        return False
if __name__=="__main__":
    main()