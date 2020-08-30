from PyQt5.QtWidgets import QPushButton, QVBoxLayout
from src import employee as e
from PyQt5.QtCore import QSettings
from src import layouts as l


class SaveButton(QPushButton):
    # Send through the main container that contains all other layouts
    def __init__(self, layout_container):
        super().__init__()
        self.setText('Save')
        settings = QSettings('Noone', 'TimeSheet')
        # Get the upper layout by using the name of the class and returning it
        upper_layout = [item for item in layout_container.children() if item.__class__.__name__ == "UpperLayout"][0]
        def save_button_clicked():
            name_text = upper_layout.name_input.text()
            class_text = upper_layout.classification_input.text()
            temp = e.Employee(name_text, class_text)
            if temp.name != "" and temp.classification != "":
                settings.setValue('Name text', temp.name)
                settings.setValue('Classification text', temp.classification)
                print("SAVED SUCCESSFULLY")
            else:
                print("FAILED TO SAVE DUE TO X")

        self.clicked.connect(save_button_clicked)
