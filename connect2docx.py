import sys
import sqlite3
from docx import Document

doc = Document('U:\LMH\Vorlage Messprotokolle\LMH-524A4101-202A1-LRT-CP-FORE HATCH MSN0000.docx')
keyword = '#filename#'

for p in doc.paragraphs:

    if keyword in p.text:
        print(p.text)
        p.text = p.text.replace(keyword, 'test')

doc.save('U:\LMH\Vorlage Messprotokolle\LMH-524A4101-202A1-LRT-CP-FORE HATCH MSN0000.docx')


def connect():
    conn = None

    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='python_mysql',
                                       user='root',
                                       password='SecurePass1!')
        if conn.is_connected():
            print('Connected to MySQL database')
    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
