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

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('drill_step_104.db')

for f in fileList:
    if f.endswith('.txt'):
        print('{} was added to the database.\n'.format(f))
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_docs(col_docName) VALUES ('" + f + "')" \
                        )
            conn.commit()
        continue
    else:
        continue
conn.close()
    


conn = sqlite3.connect('drill_step_104.db')


with conn:
    print("Here are all the .txt documents in the database: \n")
    counter = 0
    cur = conn.cursor()
    cur.execute("SELECT col_docName FROM tbl_docs WHERE LOWER(SUBSTR(col_docName,LENGTH(col_docName) - 3, 4)) = '.txt'")
    varDocs = cur.fetchall()
    for item in varDocs:
        print("{}\n".format(item[0]))
        counter += 1
    print('Total: {}'.format(counter))
     

