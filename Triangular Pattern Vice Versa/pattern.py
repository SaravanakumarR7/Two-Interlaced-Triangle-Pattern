star,hash = map(int,input("Input_Size of Star and Hash : ").split())
max_value  = max(star,hash)
patt_out = [[' '] * (2 * max_value - 1) for _ in range(max_value)]

for i in range(max_value,max_value - hash,-1):
    hash_count = hash + i - max_value
    patt = ('-' * (max_value - hash_count) + "# " * hash_count).strip()
    for j in range(len(patt)):
        patt_out[i - 1][j] = patt[j]

for i in range(star):
    flag = 0
    patt = ('-' * (max_value - star + i) + '* ' * (star - i)).strip()
    for j in range(len(patt)):
        if patt_out[i][j] == '#':
            flag = 1
        elif flag and patt[j] == '*':
            patt_out[i][j] = patt[j]
        elif flag == 0:
            patt_out[i][j] = patt[j]
for i in patt_out:
    print("".join(i))