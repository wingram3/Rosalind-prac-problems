import itertools

def all_permuatations(n):
    nums = list(range(1, n+1))
    all_perms = list(itertools.permutations(nums))
    print(len(all_perms))
    
    with open('perms.txt', 'w') as f:
        f.write(f"{len(all_perms)}\n")
        
        for perm in all_perms:
            perm_str = ' '.join(map(str, perm))
            f.write(f"{perm_str}\n")

all_permuatations(7)
