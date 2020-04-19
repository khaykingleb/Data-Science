fin = open("input.txt", "r", encoding="utf8")
fout = open("output.txt", "w", encoding="utf8")

lst = list()

for line in fin:
    a = line.split()
    lst.append([a[0], a[1], a[3]])

lst.sort()

for line in lst:
    print(" ".join(line), file=fout)

fout.close()
