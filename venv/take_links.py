from SQLite import conn, cursor
from string import Template

def filter_links():
    public = cursor.execute("SELECT name, tele_number FROM clients WHERE state='false'")

    public_ = public.fetchall()


    public_mass = []
    for name, number in public_:
        public_mass.append(name)
        public_mass.append(number)

        '''t = Template('Есімі: $name_\nБайланыс нөмірі: $number_')
        info = t.substitute(dict(name_=name, number_=number))
'''
    public_update = cursor.execute("UPDATE clients SET state = 'true'")
    conn.commit()

    return public_mass





    '''name = cursor.execute("SELECT name FROM clients")
    numbers = cursor.execute("SELECT tele_number FROM clients")
    client_names = name.fetchall()
    clients_numbers = numbers.fetchall()
    public = [client_names, clients_numbers]
    for name, number in public:
        t = Template('Есімі: $name_ Байланыс нөмірі: $number_')
        info = t.substitute(dict(name_=name, number_=number))

    return info'''

    
def clients():
    public = cursor.execute("SELECT money FROM clients ")

    public_ = public.fetchall()

    summ = 0
    for coin in public_:
        summa = int(''.join(map(str, coin)))
        summ += summa




    return  summ


    
    
