# Add whatever it is needed to interface with the DB Table corso
from model.corso import Corso
from database.DB_connect import get_connection

class Corso_DAO():
    def __init__(self):
        self._listCorsi = []
        self.ottieniCorsi()

    def ottieniCorsi(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM corso")

        for row in cursor:
            corso = Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
            self._listCorsi.append(corso)

        #print(self._listCorsi)

    def ottieniCorsiMatricola1(self, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary = True) #OGNI row DI cursor E'UN DIZIONARIO
        query = ("SELECT codins FROM iscrizione "
                 "WHERE matricola = %s")
        cursor.execute(query, (matricola,))
        listCorsiMatricola=[]
        for row in cursor:
            codins = row["codins"]
            for c in self._listCorsi:
                if c.codins == codins:
                    listCorsiMatricola.append(c)
        return listCorsiMatricola

    def ottieniCorsiMatricola2(self, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = ("SELECT c.* FROM iscrizione i, corso c "
                 "WHERE i.codins = c.codins AND matricola = %s")
        cursor.execute(query, (matricola,))
        listCorsiMatricola=[]
        for row in cursor:
            corsoMatricola = Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
            listCorsiMatricola.append(corsoMatricola)
        return listCorsiMatricola

    @property
    def listCorsi(self):
        return self._listCorsi

if __name__ == "__main__": #SERVE PER CREARE UN main DA RUNNARE IN QUESTA CLASSE (SOLO CHECK)
    corso = Corso_DAO()
    corso.ottieniCorsi()