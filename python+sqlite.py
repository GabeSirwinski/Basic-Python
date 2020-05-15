import sqlite3

conn = sqlite3.connect('drill_step_104.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_docs(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_docName TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('drill_step_104.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_docs(col_docName) VALUES ('information.docx')" \
                )
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_docs(col_docName) VALUES ('Hello.txt')" \
                )
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_docs(col_docName) VALUES ('myImage.png')" \
                )
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_docs(col_docName) VALUES ('myMovie.mpg')" \
                )
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_docs(col_docName) VALUES ('World.txt')" \
                )
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_docs(col_docName) VALUES ('data.pdf')" \
                )
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_docs(col_docName) VALUES ('myPhoto.jpg')" \
                )    
    conn.commit()
conn.close()

conn = sqlite3.connect('drill_step_104.db')


with conn:
    print("The following documents end with '.txt': \n")
    counter = 0
    cur = conn.cursor()
    cur.execute("SELECT col_docName FROM tbl_docs WHERE LOWER(SUBSTR(col_docName,LENGTH(col_docName) - 3, 4)) = '.txt'")
    varDocs = cur.fetchall()
    for item in varDocs:
        print("Document Name: {}\n".format(item[0]))
        counter += 1
    print('There are {} total.'.format(counter))
     

