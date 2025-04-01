def dig_root(n: int) -> int | None:
    s = 0
    if len(str(n)) == 1:
        s = n
        return s
    for i in str(n):
        s += int(i)
    dig_root(s)


print(dig_root(942))