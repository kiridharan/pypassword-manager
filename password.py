import sqlite3


master_password = 'YOURNAME'

passwd = str(input('ENTER THE PASSWORD: '))




def create_db():
    conn = sqlite3.connect('MAIN.db')
    print('DATABASE CREATED')

    conn.execute('''CREATE TABLE IF NOT EXISTS MAIN
        (ID INT  PRIMARY KEY    NOT NULL,
        USER            TEXT    NOT NULL,
        ACCOUNT         TEXT    NOT NULL,
        PASS            TEXT    NOT NULL);''')
     

    conn.close()

def add_bd():
    conn = sqlite3.connect('MAIN.db')
    ID      = int(input('ENTER THE NUMBER:         :'))
    ACCOUNT = str(input('ENTER THE ACCOUNT NAME    :'))
    USER    = str(input('ENTER THE USER NAME       :'))
    PASS    = str(input('eENTER THE PASSWORD NAME  :'))
    conn.execute("INSERT INTO MAIN(ID,ACCOUNT,USER,PASS) VALUES(?,?,?,?)",(int(ID) ,str(ACCOUNT),str(USER), str(PASS)))
    conn.commit()
    print('ADDED SUCCESSFULLY')
    y = int(input('ENTER 1.YES TO CONTINUE OR  2.NO END'))
    if y ==1 :
        return add_bd()
    else:
        quit
def show_db():
    conn = sqlite3.connect('MAIN.db')
    cursor = conn.execute("SELECT * from MAIN ORDER BY ID ASC")
    for row in cursor:
        print('#'*200)
        print('ID        :',row[0])
        print('USER NAME  :',row[1])
        print('ACCOUNT    :',row[2])
        print('PASSWORD   :',row[3])
        print('#'*200)
    dummy = input('PRESS ENTER TO CLOSE')
    
def update():
    conn = sqlite3.connect('MAIN.db')
    cursor = conn.execute("SELECT * from MAIN ORDER BY ID ASC")
    for row in cursor:
        print('-'*200)
        print('ID        :',row[0])
        print('USER NAME  :',row[1])
        print('ACCOUNT    :',row[2])
        print('PASSWORD   :',row[3])
        print('-'*200)
    ID = int(input('ENTER THE ID NUMBER           :'))
    USER = str(input('ENTER USER NAME             :'))
    ACCOUNT = str(input('enter the account name   :'))
    PASS = str(input('enter the PASSWORD name     :'))
    cursor.execute("UPDATE `MAIN` SET  `USER` = ?, `ACCOUNT` =?, `PASS` = ?WHERE `ID` = ?", (str(USER), str(ACCOUNT), str(PASS),str(ID)))
    conn.commit()
    cursor.execute("SELECT * FROM `MAIN` ORDER BY `ID` ASC")
    print('SUCCESSFULLY UPDATED')
    cursor.close()
    conn.close()

def delete():
    conn = sqlite3.connect('MAIN.db')
    print ("Opened database successfully")
    cursor = conn.execute("SELECT * FROM MAIN ORDER BY ID ASC")
    for row in cursor:
        print('-'*200)
        print('ID         :',row[0])
        print('USER NAME  :',row[1])
        print('ACCOUNT    :',row[2])
        print('PASSWORD   :',row[3])
        print('-'*200)
    print('DATA BASE BEFORE DELETING')
    ID = str(input('WHICH ID NUMBER SHOULD YOU NEED TO DELETE'))
    conn.execute("DELETE FROM `MAIN` WHERE ID =  %s"%ID[0])
    conn.commit()
    print ("Total number of rows deleted :", conn.total_changes)
    cursor = conn.execute("SELECT * from MAIN ORDER BY ACCOUNT ASC")
    for row in cursor:
        print('-'*200)
        print('ID         :',row[0])
        print('USER NAME  :',row[1])
        print('ACCOUNT    :',row[2])
        print('PASSWORD   :',row[3])
        print('-'*200)
    print ("DATA BASE DELETED SUCCESSFULLY")
    conn.close()


def main():
    if passwd != master_password:
        quit
    else:
        conn = sqlite3.connect('MAIN.db')
        ui = int(input('what do you want to do \n(x)ADD PASSWORDS \n(x)SHOW PASSWORDS \n(x)DELETE \n(x)UPDATE \n(x)QUIT'))
        if ui == 1:
            if __name__ == "__main__":
                create_db()
                add_bd()
        elif ui == 2:
            if __name__ == "__main__":
                show_db()
        elif ui == 3:
            if __name__ == "__main__":
                delete()
        elif ui == 4:
            if __name__ == "__main__":
                update()
        else:
            s = str(input('IF  WANNA CONTINUE TYPE y if yes (or) n if no'))
            if s == "y" or "Y":
                return main()
            else:
                quit

if __name__ == "__main__":
    main()
    
