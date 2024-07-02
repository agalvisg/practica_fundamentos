#piramideasteriscos.py

def piramide(n):
    for i in range(n):
        print(' '*(n-i-1) + '*'*(2*i+1))

def main():
    n = int(input('Introduce la altura de la pirámide: '))
    piramide(n)

    if n<0:
        print('La altura no puede ser negativa')
        return main()
    else:
        return
    
if __name__ == '__main__':
    main()