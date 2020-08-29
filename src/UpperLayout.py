from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import QSettings
from src import Employee as e


class UpperLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        settings = QSettings('Noone', 'TimeSheet')
        self.name_label = QLabel('Name:')
        self.name_input = QLineEdit(settings.value('Name text'))
        self.name_input.setMaxLength(50)
        self.classification_label = QLabel('Classification:')
        self.classification_input = QLineEdit(settings.value('Classification text'))
        self.classification_input.setMaxLength(30)
        self.save_button = QPushButton('Save')
        self.addWidget(self.name_label)
        self.addWidget(self.name_input)
        self.addWidget(self.classification_label)
        self.addWidget(self.classification_input)
        self.addWidget(self.save_button)

        def save_button_clicked():
            name_text = self.name_input.text()
            class_text = self.classification_input.text()
            temp = e.Employee(name_text, class_text)
            if temp.name != "" and temp.classification != "":
                settings.setValue('Name text', temp.name)
                settings.setValue('Classification text', temp.classification)
                print("SAVED SUCCESSFULLY")
            else:
                print("FAILED TO SAVE DUE TO X")

                pass

        self.save_button.clicked.connect(save_button_clicked)
