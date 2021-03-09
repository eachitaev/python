import sys


def itoBase(nbs, basesrc, basedst="0123456789"):
    lengthdst = len(basedst)
    lengthnbs = len(nbs)
    lengthsrc = len(basesrc)
    chislodst = 0
    newnbs = 0
    flag = True
    # Проверка правильности ввода числа в прежней системе счисления
    for i in range(0, lengthnbs):
        if basedst.find(nbs[i]) == -1:
            print("Некорректный ввод система счисления не соответсвтует заданному числу")
            flag = False
            break
    # Перевод в десятичную
    if flag == True:
        if basedst != '0123456789':
            for i in range(0, lengthnbs):
                for j in range(0, lengthdst):
                    if nbs[i] == basedst[j]:
                        newnbs = j
                        break
                chislodst = chislodst + newnbs*(lengthdst**(lengthnbs-i-1))
        else:
            chislodst = nbs
        chislodst = int(chislodst)

        # Перевод в новую систему счисления
        newnbs = ''
        while chislodst > 0:
            i = chislodst % lengthsrc
            newnbs = str(basesrc[i]) + newnbs
            chislodst //= lengthsrc
        print(newnbs)


if __name__ == '__main__':
    b = len(sys.argv)
    if b < 3:
        print("Недостаточно аргументов в командной строке")
    elif b == 3:
        nb = str(sys.argv[1])
        base = str(sys.argv[2])
        itoBase(nb, base)
    else:
        nb = str(sys.argv[1])
        base = str(sys.argv[2])
        baseDst = str(sys.argv[3])
        itoBase(nb, base, baseDst)
