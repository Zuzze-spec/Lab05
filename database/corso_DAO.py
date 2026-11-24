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

    @property
    def listCorsi(self):
        return self._listCorsi

if __name__ == "__main__": #SERVE PER CREARE UN main DA RUNNARE IN QUESTA CLASSE (SOLO CHECK)
    corso = Corso_DAO()
    corso.ottieniCorsi()