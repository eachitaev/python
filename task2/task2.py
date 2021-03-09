import sys
if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        dannie = ''
        try:
            with open(str(filename), 'r') as f:
                for word in f.readlines():
                    pass
        except:
            print("Файл не найден или его невозможно открыть")
        else:
            with open(str(filename), 'r') as f:
                for word in f.readlines():
                    dannie = word
                    print(dannie)
                    temp = []
                    num = ''
                    for char in dannie:
                        if char.isdigit() or char == '.' or char == '-':
                            num = num + char
                        else:
                            if num != '':
                                temp.append(num)
                                num = ''
                    if num != '':
                        temp.append(num)
                    temp_list = []
                    print(temp)
                    temp_list.append(dannie.find('radius'))
                    temp_list.append(dannie.find('line'))
                    temp_list.append(dannie.find('center'))
                    temp_list.append(dannie.rfind('line'))
                    temp_list = list(set(temp_list))
                    temp_list.sort()
                    temp_radius = []
                    temp_center = []
                    temp_line = []
                    temp_line_sec = []
                    for i in range(0, len(temp_list)):
                        if len(temp_list) < 4:
                            if temp_list[i] == dannie.find('radius'):
                                temp_radius.append(temp[0])
                                del temp[0]
                            if temp_list[i] == dannie.find('line'):
                                temp_line.append(temp[0:3])
                                del temp[0:3]
                                temp_line_sec.append(temp[0:3])
                                del temp[0:3]
                            if temp_list[i] == dannie.find('center'):
                                temp_center.append(temp[0:3])
                                del temp[0:3]
                        else:
                            if temp_list[i] == dannie.find('radius'):
                                temp_radius.append(temp[0])
                                del temp[0]
                            if temp_list[i] == dannie.find('line'):
                                temp_line.append(temp[0:3])
                                del temp[0:3]
                            if temp_list[i] == dannie.find('center'):
                                temp_center.append(temp[0:3])
                                del temp[0:3]
                            if temp_list[i] == dannie.rfind('line'):
                                temp_line_sec.append(temp[0:3])
                                del temp[0:3]
                    print(temp_center, temp_line, temp_radius, temp_line_sec)
                    a = temp_line
                    print(a[0], float(a[0][0]))
                    A = [float(temp_line[0][0]), float(temp_line[0][1]), float(temp_line[0][2])]
                    B = [float(temp_line_sec[0][0]), float(temp_line_sec[0][1]), float(temp_line_sec[0][2])]
                    print(B)
                    C = [float(temp_center[0][0]), float(temp_center[0][1]), float(temp_center[0][2])]
                    R = [float(temp_radius[0])]
                    a = (B[0]-A[0])**2 + (B[1]-A[1])**2 + (B[2]-A[2])**2
                    b = 2*((B[0]-A[0])*(A[0]-C[0])+(B[1]-A[1])*(A[1]-C[1])+(B[2]-A[2])*(A[2]-C[2]))
                    c = C[0]**2 + C[1]**2 + C[2]**2 + A[0]**2 + A[1]**2 + A[2]**2 - 2*(C[0]*A[0]+C[1]*A[1]+C[2]*A[2]) - \
                        R[0]**2
                    D = b**2 - 4*a*c
                    print('D = ' + str(D))
                    if D > 0:
                        D = pow(b**2 - 4*a*c, 0.5)
                        ufirst = (-b + D)/(2*a)
                        usecond = (-b - D)/(2*a)
                        x = A[0] + ufirst*(B[0]-A[0])
                        y = A[1] + ufirst*(B[1]-A[1])
                        z = A[2] + ufirst*(B[2]-A[2])
                        x2 = A[0] + usecond*(B[0]-A[0])
                        y2 = A[1] + usecond*(B[1]-A[1])
                        z2 = A[2] + usecond*(B[2]-A[2])
                        print('['+ str(x) +', ' + str(y) + ', ' + str(z) + ']'', ''[' + str(x2) + ', ' + str(y2)+ ', ' +
                              str(z2) +']')
                    if D == 0:
                        ufirst = (-b) / (2 * a)
                        x = A[0] + ufirst * (B[0] - A[0])
                        y = A[1] + ufirst * (B[1] - A[1])
                        z = A[2] + ufirst * (B[2] - A[2])
                        print('[' + str(x) + ', ' + str(y) + ', ' + str(z) + ']')
                    if D < 0:
                        print("Колизий не найдено ")
