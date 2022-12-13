x = int(input("Adj meg egy számot!"))
y = int(input("Add meg a második számot!"))

if x<0 and y<0:
    print("A mind a két szám negatív")
elif x<0 and y>=0:
    print("A két szám közül az első negatív")
elif y<0 and x>=0:
    print("A két szám közül a második negatív")
else:
    print("A két szám közül egyik sem negatív")