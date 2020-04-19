fin = open('input.txt', 'r', encoding='utf-8-sig')
fout = open('output.txt', 'w', encoding='utf-8')
k = int(fin.readline())
i = 0
st1 = []
for line in fin:
    ex1, ex2, ex3 = line.split()[-3:]
    if int(ex1) >= 40 and int(ex2) >= 40 and int(ex3) >= 40:
        st = int(ex1) + int(ex2) + int(ex3)
        st1.append(st)
if len(st1) <= k:
    print(0, file=fout)
else:
    st1.sort(reverse=True)
    while k > 0:
        if st1[k-1] == st1[k]:
            k -= 1
        else:
            print(st1[k-1], file=fout)
            break
    if k == 0:
        print(1, file=fout)
fout.close()
fin.close()
