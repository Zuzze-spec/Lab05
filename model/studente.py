class Studente:

    def __init__(self, matricola, cognome, nome, CDS):
        self._matricola = matricola
        self._cognome = cognome
        self._nome = nome
        self._CDS = CDS

    def __str__(self):
        return f"{self._nome.upper()}, {self._cognome.upper()} ({self._matricola})"

    @property
    def cognome(self):
        return self._cognome

    @property
    def nome(self):
        return self._nome