
substrings=[]
with open('shortest_superstring.txt','r') as f:
    f.readline()
    curr = ''
    line = f.readline().strip()
    while line != '':
        if line[0] == ">":
            substrings.append(curr)
            curr = ''
        else:
            curr += line
        line = f.readline().strip()
    substrings.append(curr)

print(substrings)

def shortestSuperstring(seqs):
    left = [i for i in range(1, len(seqs))]
    candidate = seqs[0]
    while len(left) > 0:
        for i in left:
            before = True
            after = True
            for j in reversed(range(int(len(seqs[i]) / 2), len(seqs[i]))):
                if after:
                    if candidate.endswith(seqs[i][:j]):
                        candidate = candidate + seqs[i][j:]
                        left.remove(i)
                        after = False
                if before:
                    if seqs[i].endswith(candidate[:j]):
                        candidate = seqs[i][:-j] + candidate
                        left.remove(i)
                        before = False
    return candidate

print(shortestSuperstring(substrings))
