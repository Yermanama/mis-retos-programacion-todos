
def decimal_oct(numero : int):
    return oct(numero)[2:]

def decimal_hexa(numero: int):
    return hex(numero)[2:]

if __name__ == "__main__":
    print(decimal_hexa(24))
    print(decimal_oct(24))
