def get_indices(s, c):
    c = c.lower()
    return [i for i, x in enumerate(s) if x == c]

s = input()
t = input()

if t[2] == "X":
    indice1 = get_indices(s, t[0])
    indice2 = get_indices(s, t[1])
    if indice1 == [] or indice2 == []:
        print("No")
        exit()
    if indice1[0] < indice2[-1]:
        print("Yes")
    else:
        print("No")

else:
    indice1 = get_indices(s, t[0])
    indice2 = get_indices(s, t[1])
    indice3 = get_indices(s, t[2])
    if indice1 == [] or indice2 == [] or indice3 == []:
        print("No")
        exit()
    indexd1 = indice1[0]
    index3 = indice3[-1]
    for i in indice2:
        if indexd1 < i and i < index3:
            print("Yes")
            exit()
    print("No")