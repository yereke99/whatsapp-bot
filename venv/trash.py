for i in a:
    if len(i) == 10:
        if not '.' in i:
            where = int(a.index(i))
            print("Төлем құны: " + a[0] + a[1])
            print("Квитанция: ", a[where])
            summ = a[0] + a[1]
            SUMM = ''.join(summ)
            KVI = a[where]
            kvi = ''.join(KVI)
            # cursor.execute("INSERT INTO client (money) VALUES (%s)", (SUMM,))
            # cursor.execute("INSERT INTO client (kvi) VALUES (%s)", (kvi,))
            # db.commit()

        if '.' in i:
            where_ = int(a.index(i))
            print("Дата: ", a[where_])
            data = a[where_]
            DATA = ''.join(data)
            # cursor.execute("INSERT INTO client (data) VALUES (%s)", (DATA,))
            # db.commit()
    if len(i) == 5:
        if ':' in i:
            _where = int(a.index(i))
            print("Төлем уақыты: ", a[_where])
            time = a[_where]
            TIME = ''.join(time)
            # cursor.execute("INSERT INTO client (time) VALUES (%s)", (TIME,))
            # db.commit()
            print("Кім жіберді: ", a[_where + 1], a[_where + 2])
            who = a[_where + 1] + a[_where + 2]
            WHO = ''.join(who)
            # cursor.execute("INSERT INTO client (who) VALUES (%s)", (WHO,))
            # db.commit()

    if len(i) == 9 and '-' in i:
        # if '-' in i:
        where__ = int(a.index(i))
        print("Қабылдаушы номері: ", a[where__ - 2], a[where__ - 1], a[where__])
        number = a[where__ - 2] + a[where__ - 1] + a[where__]
        str_number = ''.join(number)
        # cursor.execute("INSERT INTO client (money, kvi, data, time, who, owner_number) VALUES (%s, %s, %s, %s, %s, %s)", (SUMM, kvi, DATA, TIME, WHO, str_number))
        # db.commit()

    if '*9908' in i:
        _owner_name = "Дәурен"
        cursor.execute("INSERT INTO client (money, kvi, data, time, who, owner_name) VALUES (%s, %s, %s, %s, %s, %s)",
                       (SUMM, kvi, DATA, TIME, WHO, _owner_name,))
        db.commit()


