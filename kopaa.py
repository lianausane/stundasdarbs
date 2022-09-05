import liana

x = int(input("Izvēlies vienu no figūrām, kuru aprēķināsi: riņķis-1 , trijstūris-2 , taisnstūris-3: "))
if x==1:
    y = int(input("Izvēlies, ko aprēķināsi;laukums-1, riņkā līnijas garums-2 , diametrs-3: "))
    if y==1:
        a = int(input("Ievadi rādiusu:"))
        print("Laukums ir", liana.rinka_lauk(a))
    elif y==2:
        b = int(input("Ievadi rādiusu:"))
        print("Perimetrs ir", liana.rinka_perimets(b))
    else:
        c = int(input("Ievadi rādiusu:"))
        print("Diametrs ir", liana.rinka_diamet(c))
elif x == 2:
    m = int(input("Izvēlies, ko aprēķināsi;laukums-1, perimetrs-2 :  "))
    if m==1:
        d = int(input("Ievadi trijstrūra augstumu(h): "))
        k = int(input("Ievadi trijstrūra malas garumu: "))
        print("Laukums ir", liana.trijs_laukums(d, k))
    else:
        a = int(input("Ievadi trijstrūra pirmo malu: "))
        b = int(input("Ievadi trijstrūra otro malu: ")) 
        c = int(input("Ievadi trijstrūra trešo malu: "))
        print("Perimetrs ir", liana.trijs_perimetrs(a, b, c))
else:
    g = int(input("Izvēlies, ko aprēķināsi;laukums-1, perimetrs-2, :  ")) 
    if g == 1:
        u = int(input("Ievadi taisnustūta īsāko malu: "))
        t = int(input("Ievadi taisnustūta garāko malu: "))
        print("Laukums ir", liana.cetrusturis_laukums(u, t))
    else: 
        u = int(input("Ievadi taisnustūta īsāko malu: "))
        t = int(input("Ievadi taisnustūta garāko malu: "))
        print("Perimetrs ir", liana.cetrusturis_perimetrs(u, t))