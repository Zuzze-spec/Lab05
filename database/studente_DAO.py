# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


class Studente_DAO:
    def __init__(self):
        pass

    def ottieniStudentiCorso(self, codinsCorso):
        cnx= get_connection() #CONNESSIONE AL DATABASE (SEMPRE UGUALE)
        cursor = cnx.cursor(dictionary=True) #SERVE PER LEGGERE DEL DB E LE SALVA COME dictionary
        query = ("select s.* from studente s, iscrizione i "
                 "where s.matricola = i.matricola and i.codins = %s") #%s E' VARIABILE A SECONDA DEL codinsCorso
        cursor.execute(query, (codinsCorso,)) #PER REGOLE SINTATTICHE CI VUOLE LA ,

        listStudenti = []
        for row in cursor:
            listStudenti.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        return listStudenti

    @property
    def listStudenti(self):
        return self._listStudenti
