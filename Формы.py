'''  Полностью проходят первые 13 тестов. Во всех остальных программа
пишет немного лишнего, но все нужные половинки есть '''

f = open(r"C:\Users\Halim\OneDrive\Рабочий стол\Олимпиадки\Тесты к задачам и мои заметки\Формы\Формы для отливки\input19.txt")
lines_dirty = f.readlines()
f.close()
lines = lines_dirty

for i in range(len(lines)):
    if i == len(lines)-1:
        lines[i] = lines_dirty[i][:len(lines_dirty[i])].replace(" ", "")
    else:
        lines[i] = lines_dirty[i][:len(lines_dirty[i])-1].replace(" ", "")  # убрал /n в конце каждой строки и все пробелы
i = 0

n = int(lines[0])
rez = []  # Это список списков l, по порядку для каждой целой

for i in range(1, n+1):
    form = lines[i]
    a, b, c, d = form[:5], form[5:10], form[10:15], form[15:20]  # Обычные стороны формы
    ar, br, cr, dr = form[4::-1], form[9:4:-1], form[14:9:-1], form[19:14:-1]  # Перевёрнутые стороны формы
    sides = [a, b, c, d]
    sides_reverse = [ar, br, cr, dr]

    halfs =[[a, b, c],  # Половинки обычной формы
            [c, d, a],
            [d, a, b],
            [b, c, d],
            [c, b, a],
            [a, d, c],
            [b, a, d],
            [d, c, b],
            [ar, dr, cr],  # Половинки перевёрнутой формы
            [cr, br, ar],
            [br, ar, dr],
            [dr, cr, br],
            [ar, br, cr],
            [cr, dr, ar],
            [dr, ar, br],
            [br, cr, dr]]

    l = []  # Это список, в котором будут номера половинок, подходящих для конкретной целой
    lh = []  # Это список, в котором будут сами половинки, подходящие для конкретной целой

    for j in range(n+1, 3*n+1):
        half = [lines[j][:5], lines[j][5:10], lines[j][10:15]]
        if half in halfs:
            lh.append(half)
            l.append(j-n)  # Тут всегда есть нужные, надо только отфильтровать

    l_temp = []  # Этот список нужен, чтобы складывать туда номера стыкующихся и вычислить предателя

    for f in range(len(l) - 1):
        for g in range(f + 1, len(l)):

            if lh[f][0] == lh[g][2] and lh[f][2] == lh[g][0]: # Первый вариант стыковки
                sides_copy = sides.copy()
                sides_reverse_copy = sides_reverse.copy()

                if lh[f][0] in sides and lh[f][2] in sides and lh[f][1] in sides and lh[g][1] in sides:
                    sides_copy.remove(lh[f][0])
                    sides_copy.remove(lh[f][2])
                    if lh[f][1] in sides_copy and lh[g][1] in sides_copy:
                        if (sides_copy.index(lh[f][1])) != (1 - sides_copy[::-1].index(lh[g][1])): # Индекс первого вхождения первой середины не равен индексу последнего вхождения второй середины
                            if l[f] not in l_temp:
                                l_temp.append(l[f])
                            if l[g] not in l_temp:
                                l_temp.append(l[g])

                elif lh[f][0] in sides_reverse and lh[f][2] in sides_reverse and lh[f][1] in sides_reverse and lh[g][1] in sides_reverse:
                    sides_reverse_copy.remove(lh[f][0])
                    sides_reverse_copy.remove(lh[f][2])
                    if lh[f][1] in sides_reverse_copy and lh[g][1] in sides_reverse_copy:
                        if (sides_reverse_copy.index(lh[f][1])) != (1 - sides_reverse_copy[::-1].index(lh[g][1])): # Индекс первого вхождения первой середины не равен индексу последнего вхождения второй середины
                            if l[f] not in l_temp:
                                l_temp.append(l[f])
                            if l[g] not in l_temp:
                                l_temp.append(l[g])

            if lh[f][0][::-1] == lh[g][0] and lh[f][2][::-1] == lh[g][2]:  # Второй вариант стыковки
                sides_copy = sides.copy()
                sides_reverse_copy = sides_reverse.copy()

                if lh[f][0] in sides_reverse and lh[f][2] in sides_reverse and lh[f][1] in sides_reverse and lh[g][1] in sides: # Если f перевёрнута, а g нет
                    sides_copy.remove(lh[g][0])
                    sides_copy.remove(lh[g][2])
                    if lh[f][1][::-1] in sides_copy and lh[g][1] in sides_copy:
                        if (sides_copy.index(lh[f][1][::-1])) != (1 - sides_copy[::-1].index(lh[g][1])): # Индекс первого вхождения первой середины не равен индексу последнего вхождения второй середины
                            if l[f] not in l_temp:
                                l_temp.append(l[f])
                            if l[g] not in l_temp:
                                l_temp.append(l[g])

                elif lh[f][0] in sides and lh[f][2] in sides and lh[f][1] in sides and lh[g][1] in sides_reverse: # Если g перевёрнута, а f нет
                    sides_copy.remove(lh[f][0])
                    sides_copy.remove(lh[f][2])
                    if lh[f][1] in sides_copy and lh[g][1][::-1] in sides_copy:
                        if (sides_copy.index(lh[f][1])) != (1 - sides_copy[::-1].index(lh[g][1][::-1])): # Индекс первого вхождения первой середины не равен индексу последнего вхождения второй середины
                            if l[f] not in l_temp:
                                l_temp.append(l[f])
                            if l[g] not in l_temp:
                                l_temp.append(l[g])

    if len(l_temp) == 0:
        print(l_temp, l)
    rez.append(l_temp)
print()

list_halfs = []
for y in range(n + 1, 3 * n + 1):
    list_halfs.append([lines[y][:5], lines[y][5:10], lines[y][10:15]])

for p in range(1):

    for h in range(len(rez)):
        if len(rez[h]) == 2:
            for e in range(2):
                for o in range(len(rez)):
                    if rez[h][e] in rez[o] and h != o:
                        rez[o].remove(rez[h][e])

for n in rez:
    for m in n:
        print(m, end=" ")
    print()
