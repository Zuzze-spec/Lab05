import flet as ft
from pygments.styles.night_owl import blue


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._ddCorso = None
        self._bCercaIscritti = None
        self._matricola = None
        self._nome = None
        self._cognome = None
        self._bCercaStudente = None
        self._bCercaCorsi = None
        self._bIscrivi = None
        self._lv = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        self._ddCorso = ft.Dropdown(value=None,
                                    label="corso",
                                    expand=True,
                                    hint_text="corso",
                                    options=self._controller.riempiDD())
        self._bCercaIscritti = ft.ElevatedButton(text="Cerca Iscritti",
                                                 color="blue",
                                                 on_click=self._controller.cercaIscritti)
        row1 = ft.Row(controls=[self._ddCorso, self._bCercaIscritti])

        self._matricola = ft.TextField(value=None,
                                       label="matricola",
                                       width=150)
        self._nome = ft.TextField(value=None,
                                  label="nome")
        self._cognome = ft.TextField(value=None,
                                     label="cognome")
        row2 = ft.Row(controls=[self._matricola, self._nome, self._cognome])

        self._bCercaStudente = ft.ElevatedButton(text="Cerca studente",
                                                 color="blue",
                                                 on_click=self._controller.cercaStudente)
        self._bCercaCorsi = ft.ElevatedButton(text="Cerca corsi",
                                              color="blue",
                                              on_click=self._controller.cercaCorsi)
        self._bIscrivi = ft.ElevatedButton(text="Iscrivi",
                                           color="blue",
                                           on_click=self._controller.iscrivi)
        row3 = ft.Row(controls=[self._bCercaStudente, self._bCercaCorsi, self._bIscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        self._page.add(row1, row2, row3, self._lv)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
