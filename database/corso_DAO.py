# Add whatever it is needed to interface with the DB Table corso
from model.corso import Corso
from model.studente import Studente
from database.DB_connect import get_connection

def leggiCorsiDalDB( mappaCorsi):
    cnx = get_connection()
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute('SELECT * FROM corso')
        for row in cursor:
            cTemp = Corso(row['codins'], row['crediti'], row['nome'] ,row['pd'])
            mappaCorsi[cTemp.codins] = cTemp
        cursor.close()
        cnx.close()
        return mappaCorsi
    else:
        print('Errore nella lettura del DB')
        return None

def getIscritti(codins):
    cnx = get_connection()
    iscritti = []
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        query=("""SELECT studente.* FROM studente,iscrizione
                  WHERE studente.matricola=iscrizione.matricola 
                  AND iscrizione.codins=%s""")
        cursor.execute(query, (codins,))
        for row in cursor:
            sTemp = Studente( row['matricola'], row['nome'], row['cognome'], row['CDS'])
            iscritti.append(sTemp)
        cursor.close()
        cnx.close()
        return iscritti
    else:
        print('Errore nella lettura del DB')
        return None

def iscriviCorso(matricola, codins):
    cnx = get_connection()
    result = []
    query = """INSERT IGNORE INTO `iscritticorsi`.`iscrizione` 
       (`matricola`, `codins`) 
       VALUES(%s,%s)
       """
    if cnx is not None:
        cursor = cnx.cursor()
        cursor.execute(query, (matricola, codins,))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    else:
        print("Could not connect")
        return False