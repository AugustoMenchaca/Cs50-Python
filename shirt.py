import os, sys
os.system('cls')
from PIL import Image, ImageOps
from pizza import verificar
def png():
    shirt=Image.open("shirt.png")
    return shirt
def main():
    if len(sys.argv)==1 or len(sys.argv)==2:
        sys.exit("Too few arguments in line")
    elif len(sys.argv)>=4:
        sys.exit("Too many arguments in line")
    else:
        ImageI=sys.argv[1]
        ImageF=sys.argv[2]
        if verificar(ImageF):
            sys.exit("This file already exist")
        if verificar(ImageI):
            try:
                with Image.open(ImageI)as img:
                    fitted = ImageOps.fit(img,(600,600),Image.LANCZOS)
                    shirt=png()
                    fitted.paste(shirt,shirt)
                    fitted.save(ImageF)
                    print(ImageF)
            except Exception as e:
                sys.exit(f"Error : {e}")
main()
