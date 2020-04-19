fin = open("input.txt", encoding="utf8")
fout = open("output.txt", "w", encoding="utf8")

candidates = dict()
votes = 0
for line in fin:
    line = line.rstrip()
    candidates[line] = candidates.get(line, 0) + 1
    votes += 1

sort_key = sorted(candidates, key=lambda x: candidates[x], reverse=True)

if candidates[sort_key[0]] / votes > 0.5:
    print(sort_key[0], file=fout)
else:
    print(sort_key[0], sort_key[1], sep="\n", file=fout)
