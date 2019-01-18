
import sys
from app.services import storage_service as ss
from app.domain.athlete import Athlete
from app.domain.injury import Injury
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot


class AddAthleteForm(QWidget):
    def __init__(self):
        super(AddAthleteForm, self).__init__()
        loadUi("add_athlete_form.ui", self)


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("gui.ui", self)

        self.set_up_ui()


    def set_up_ui(self):
        """Setting up UI"""
        self.refresh_athletes_list()
        self.add_athlete_button.clicked.connect(self.on_add_athlete_button_clicked)
        self.add_injury_button.clicked.connect(self.on_add_injury_clicked)
        self.delete_athlete_button.clicked.connect(self.on_delete_athlete_button_clicked)
        self.get_injuries_button.clicked.connect(self.on_get_injuries_button_clicked)

    def on_add_injury_clicked(self):
        pass

    def on_delete_athlete_button_clicked(self):
        selected_items = self.athletes_list_widget.selectedItems()
        for item in selected_items:
            for athlete in self.athletes:
                if item.text() == f"{athlete.first_name} {athlete.last_name}":
                    ss.remove(athlete.id)
        self.refresh_athletes_list()

    def on_get_injuries_button_clicked(self):
        pass

    def on_add_athlete_button_clicked(self):
        """Action for the add athlete button"""
        self.add_athlete_form = AddAthleteForm()
        self.add_athlete_form.show()
        self.add_athlete_form.add_button.clicked.connect(self.on_add_button_clicked)

    def on_add_button_clicked(self):
        """Action for the add button in the add athlete form"""
        first_name = self.add_athlete_form.first_name_edit.text()
        last_name = self.add_athlete_form.last_name_edit.text()
        if not first_name or not last_name:
            message = "<html><head/><body><p align='center'><span style=' font-size:12pt; font-weight:600;" \
                      " color:#ff0000;'>Some fields are missing!</span></p></body></html>"
            self.add_athlete_form.notification.setText(message)
        else:
            ss.add_athlete(Athlete.default_constructor(first_name, last_name))
            self.refresh_athletes_list()
            self.add_athlete_form.close()

    def refresh_athletes_list(self):
        """Refreshes the list widget"""
        athletes = ss.get_athletes()
        self.athletes = athletes
        self.athletes_list_widget.clear()
        if not athletes:
            message = "<html><head/><body><p align='center'><span style=' font-size:12pt; font-weight:600;" \
                      " color:#ff0000;'>There are no athletes in the list. Please, add them!</span></p></body></html>"
            self.notification.setText(message)
        else:
            message = "<html><head/><body><p align='center'><span style=' font-size:12pt; font-weight:600;" \
                      " color:#000;'>Athletes View</span></p></body></html>"
            self.notification.setText(message)
            for athlete in athletes:
                item = QListWidgetItem(f"{athlete.first_name} {athlete.last_name}")
                self.athletes_list_widget.addItem(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
