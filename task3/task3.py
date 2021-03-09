import sys, datetime, re, csv

#Результирующий класс
class Result:
    def __init__(self):
        self.try_top = 0
        self.fail_top = 0
        self.proc_top = 0
        self.v_top_succes = 0
        self.v_top_fail = 0
        self.try_scoop = 0
        self.proc_scoop = 0
        self.fail_scoop = 0
        self.v_scoop_succes = 0
        self.v_scoop_fail = 0
        self.v_begin = 0
        self.v_end = 0

#Перевод времени в datetime
def arg_to_datetime(firstdate):
    new_date = ''
    new_date = firstdate.replace('Z', ':').replace('.', ':').replace('T', ':').replace('-', ':')
    if new_date.find(':'):
        new_date = new_date.split(':')
    if len(new_date) < 7:
        for i in range(len(new_date), 7):
            new_date.append('0')
    if new_date[1] == '0':
        new_date[1] = '1'
    if new_date[2] == '0':
        new_date[2] = '1'
    time = datetime.datetime(year=int(new_date[0]), month=int(new_date[1]), day=int(new_date[2]),
                             hour=int(new_date[3]), minute=int(new_date[4]), second=int(new_date[5]),
                             microsecond=int(new_date[6])*1000)
    return time

# Нахождение литров в логе
def arg_to_rascV(findv):
    temp = []
    num = ''
    tempfindv = findv
    tempfindv = tempfindv[tempfindv.rfind('-'):]
    for char in tempfindv:
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                temp.append(int(num))
                num = ''
    if num != '':
        temp.append(int(num))
    return temp


if __name__ == '__main__':
    filename = sys.argv[1]
    ResultV = Result()
    ResultVBgEnd = Result()
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        count = 0
        try:
            firstdate = arg_to_datetime(sys.argv[2])
            seconddate = arg_to_datetime(sys.argv[3])
        except:
            print("Неправильный формат данных")
            print("Пример данных ./log.log 2020-01-01T12:00:00 2020-01-01T13:00:00")
        else:
            a = []
            b = ''
            temp_per = ''
            date_temp_per = ''
            try:
                with open(str(filename), 'r') as f:
                    for word in f.readlines():
                        pass
            except:
                print("Файл не найден или его невозможно открыть")
            else:
                with open(str(filename), 'r') as f:
                    for word in f.readlines():
                        # Нахождение объёма в лог файле
                        if word.find('объём') != -1:
                            a.append(word)
                        if word.find('wanna') != -1:
                            count = count + 1
                            temp_per = word.split('Z')
                            date_temp_per = arg_to_datetime(temp_per[0])
                            # Нахождение ископых параметров
                            if (date_temp_per <= seconddate) and (date_temp_per >= firstdate):
                                arg_temp_per = arg_to_rascV(temp_per[1])
                                if temp_per[1].find('top') != - 1:
                                    ResultV.try_top = ResultV.try_top + 1
                                    if temp_per[1].find('фейл') != - 1:
                                        ResultV.fail_top = ResultV.fail_top + 1
                                        ResultV.v_top_fail = ResultV.v_top_fail + int(arg_temp_per[0])
                                    else:
                                        ResultV.v_top_succes = ResultV.v_top_succes + int(arg_temp_per[0])
                                else:
                                    ResultV.try_scoop = ResultV.try_scoop + 1
                                    if temp_per[1].find('фейл') != - 1:
                                        ResultV.fail_scoop = ResultV.fail_scoop + 1
                                        ResultV.v_scoop_fail = ResultV.v_scoop_fail + int(arg_temp_per[0])
                                    else:
                                        ResultV.v_scoop_succes = ResultV.v_scoop_succes + int(arg_temp_per[0])
                f.close()
                count = 0
                with open(str(filename), 'r') as f:
                    for word in f.readlines():
                        if word.find('wanna') != -1:
                            count = count + 1
                            temp_per = word.split('Z')
                            date_temp_per = arg_to_datetime(temp_per[0])
                            if date_temp_per < firstdate:
                                arg_temp_per = arg_to_rascV(temp_per[1])
                                if temp_per[1].find('top') != - 1:
                                    ResultVBgEnd.try_top = ResultVBgEnd.try_top + 1
                                    if temp_per[1].find('фейл') != - 1:
                                        ResultVBgEnd.fail_top = ResultVBgEnd.fail_top + 1
                                        ResultVBgEnd.v_top_fail = ResultVBgEnd.v_top_fail + int(arg_temp_per[0])
                                    else:
                                        ResultVBgEnd.v_top_succes = ResultVBgEnd.v_top_succes + int(arg_temp_per[0])
                                else:
                                    ResultVBgEnd.try_scoop = ResultVBgEnd.try_scoop + 1
                                    if temp_per[1].find('фейл') != - 1:
                                        ResultVBgEnd.fail_scoop = ResultVBgEnd.fail_scoop + 1
                                        ResultVBgEnd.v_scoop_fail = ResultVBgEnd.v_scoop_fail + int(arg_temp_per[0])
                                    else:
                                        ResultVBgEnd.v_scoop_succes = ResultVBgEnd.v_scoop_succes + int(arg_temp_per[0])

                b = a[0].find('(')
                a[0] = a[0][0:b].replace(' ', '')
                b = a[1].find('(')
                a[1] = a[1][0:b].replace(' ', '')
                V_bochki = int(a[0])
                V_tek = int(a[1])
                V_temp = 0
                if V_tek >= V_bochki:
                    V_temp = V_tek
                    V_tek = V_bochki
                    V_bochki = V_temp
                ResultVBgEnd.v_begin = ResultVBgEnd.v_top_succes + V_tek - ResultVBgEnd.v_scoop_succes
                ResultVBgEnd.v_end = ResultVBgEnd.v_begin + ResultV.v_top_succes - ResultV.v_scoop_succes
                if ResultV.try_top != 0:
                    ResultV.proc_top = (ResultV.fail_top/ResultV.try_top) * 100
                    print(ResultV.fail_top, ResultV.proc_top, ResultV.v_top_fail)
                if ResultV.try_scoop != 0:
                    ResultV.proc_top = (ResultV.fail_scoop / ResultV.try_scoop) * 100
                MyData = [["Количество попыток налить воду в бочку за период " + sys.argv[2] + "-" + sys.argv[3],
                          "Процент ошибок налития воды в бочку", "Объем воды налитый в бочку", "Объем воды не налитый в бочку",
                          "Количество попыток забрать воду из бочки за период " + sys.argv[2] + "-" + sys.argv[3],
                         "Процент ошибок забора воды из бочки", "Объем воды забранный из бочки",
                         "Объем воды не забранный из бочки", "Объём воды в бочке в начале отрезка",
                         "Объём воды в бочке в конце отрезка"],
                        [ResultV.try_top, ResultV.proc_top, ResultV.v_top_succes, ResultV.v_top_fail,
                         ResultV.try_scoop, ResultV.proc_scoop, ResultV.v_scoop_succes, ResultV.v_scoop_fail,
                          ResultVBgEnd.v_begin, ResultVBgEnd.v_end]]
                MyFile = open('ResultTask3.csv', 'w')
                with MyFile:
                    writer = csv.writer(MyFile)
                    writer.writerows(MyData)
                MyFile.close()



