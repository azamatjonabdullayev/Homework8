print("Salom")
print("Dunyo")

def sonalar(son: int) -> int:
    return son//2

print(sonalar(16))


def tub(son: int) -> bool:
    a = 0
    for i in range(1, son+1):
        if son % i == 0:
            a += 1

    if a == 2:
        return True
    else: return False


print(tub(13))