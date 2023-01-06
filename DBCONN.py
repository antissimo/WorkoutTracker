import mysql.connector

def ConnectToDataBase():
    config = {
        'user': 'korisnicko_ime',
        'password': 'lozinka',
        'host': 'localhost',
        'database': 'ime_baze',
        'raise_on_warnings': True
    }
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Pogrešno korisničko ime ili lozinka")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Baza podataka ne postoji")
        else:
            print(err)
    else:
        return cnx

cnx = ConnectToDataBase()




def FetchData(cnx, tablica):
    cursor = cnx.cursor()
    upit = "SELECT * FROM " + tablica
    cursor.execute(upit)
    podaci = cursor.fetchall()
    return podaci




podaci = FetchData(cnx, "tablica")