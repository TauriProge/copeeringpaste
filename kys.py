ruut = []
for _ in (1,2,3):
    rida = input()   
    ruut.append(list(rida))
for i in ruut:
    print(i)
yloc=-1
for y in ruut:
    yloc += 1
    xloc=0
    for x in y:
        if "K" in y:
            if xloc > y.index("K"):
                while yloc != -1:
                    ruut[yloc][xloc]="."
                    yloc -= 1
        xloc += 1


