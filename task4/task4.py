import sys
#a = 'afdsfsuh'#hkjklkg'
#b = ''
if __name__ == '__main__':    
    try:
        a = str(sys.argv[1])
    except:
        print("Пустая строка в 1 аргументе")
    else:
        try:
            b = str(sys.argv[2])
        except:
            print("КО")
        else:
            c = b.split('*')
            flag = 'ОК'
            index = 0
            if len(c) == 1:
                index = a.find(c[0], index)
                if index != 0:
                    flag = 'КО'
                index = index + len(c[0])
                if index != len(a):
                    flag = 'КО'
            if len(c) > 1:
                if c[0] != '':
                    index = a.find(c[0], index)
                    if index != 0:
                        flag = 'КО'
                for i in range(1, len(c)-1):
                    if c[i] != '':
                        index = a.find(c[i], index)
                        if index == -1:
                            flag = 'КО'
                            break
                        index = index + len(c[i])
                if c[-1] != '':
                    index = a.rfind(c[-1], index)
                    if index == -1:
                        flag = 'КО'
                    index = index + len(c[-1])
                    if index != len(a):
                        flag = 'КО'
                print(flag)
