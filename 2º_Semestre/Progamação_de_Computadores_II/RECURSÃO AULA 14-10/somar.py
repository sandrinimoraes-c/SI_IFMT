def somar (num):
    if num ==0:
        return 1
    return num + somar(num-1)

print(somar(3))