import cv2, re
import pytesseract
import wget
import requests, shutil
from time import sleep
from pdf_2_image_ocr import pdf_2_image
from time import sleep
from SQLite import conn, cursor

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
config = r'--oem 3 --psm 6'
#URL = "https://api.twilio.com/2010-04-01/Accounts/AC546a11d5692dbd9828057a183e77c185/Messages/MM65d9498d7826d18ff8d3ddcd91f036b6/Media/ME69a1b957af583072d511bb65e4960e41"



def download(url, n):
    global number
    number = n
    file_name = url.split("/")[-1]
    formats = ".pdf"
    file_name += formats
    print(file_name)
    
    r = requests.get(url, stream=True)

    if r.status_code == 200:

        r.raw.decode_content = True

        with open(file_name, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print(f"PDF file successfully downloaded {file_name}: ".format(file_name))
        pdf_2_image(file_name)

    else:
        print("Error!")


    #return file_name



def recognition_text(imgs):
    IMAGE = cv2.imread(imgs)
    #crop = IMAGE[1400:3000, 200:1995]

    img = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2RGB)

    ret, black_white = cv2.threshold(img, 127, 255, 0)
    #cv2.imshow('result', black_white)
    text = pytesseract.image_to_string(black_white, lang='rus', config=config)

    a = re.split('\s+', text)



    for i in a:
        if '1' and '000,00' in i:
            owner = 'Дәурен'
            print("Кімге: " + owner)

            for an in a:

                if len(an)  == 10:
                    if not '.' in an:
                        where = int(a.index(an))
                        kvi = a[where]
                        KVI = ''.join(kvi)
                        print("Квитанция: " + KVI)



                if len(an) == 10:
                    if '.' in an:
                        where = int(a.index(an))
                        data = a[where]
                        DATA = ''.join(data)
                        print("Дата: " + DATA)
                if len(an) == 5:
                    if ':' in an:
                        where = int(a.index(an))
                        time = a[where]
                        who_send = a[where + 1]
                        WHO = ''.join(who_send)
                        TIME = ''.join(time)
                        print("Уақыты: " + TIME)
                        print("Кім жіберді: " + WHO)
                        try:
                            cursor.execute("""
                                                                   INSERT INTO clients(money, 
                                                                                       kvi,
                                                                                       name,
                                                                                       data,
                                                                                       time,
                                                                                       tele_number,
                                                                                       state) VALUES(?,?,?,?,?,?,?)
                                                    """, ('1000', KVI, WHO, DATA, TIME, str(number), 'false'))
                            conn.commit()


                        except Exception as e:
                            cursor.execute("""
                                                                   INSERT INTO clients(money, 
                                                                                       kvi,
                                                                                       name,
                                                                                       data,
                                                                                       time,
                                                                                       tele_number, 
                                                                                       state) VALUES(?,?,?,?,?,?,?)
                                                    """, ('1000', 'no kvi', WHO, DATA, TIME, str(number), 'false'))
                            conn.commit()


    print(a)
    return text


