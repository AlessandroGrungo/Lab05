# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente
def getCorsi(matricola):
    cnx = get_connection()
    corsi = []
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT corso.* FROM iscrizione, corso
                    WHERE iscrizione.matricola=%s AND corso.codins=iscrizione.codins"""
        cursor.execute(query, (matricola,))
        for row in cursor:
            if row is not None:
                cTemp = Corso(row['codins'], row['crediti'], row['nome'], row['pd'])
                corsi.append(cTemp)
        cursor.close()
        cnx.close()
        return corsi
    else:
        print("Errora di lettura dal DB")
        return None

def leggiStudentiDalDB(mappaStudenti):
    cnx = get_connection()
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute('SELECT * FROM studente')
        for row in cursor:
            sTemp = Studente(row['matricola'], row['cognome'], row['nome'], row['CDS'])
            mappaStudenti[sTemp.matricola] = sTemp
        cursor.close()
        cnx.close()
        return mappaStudenti
    else:
        print('Errore nella lettura del DB')
        return {}
