from PyQt5.QtWidgets import QPushButton
from src import employee as e
from PyQt5.QtCore import QSettings
from src import layouts as l


class SaveButton(QPushButton):
    # Send through the main container that contains all other layouts
    def __init__(self, layout_container):
        super().__init__()
        self.setText('Save')
        settings = QSettings('Noone', 'TimeSheet')
        upper_frame = None
        for i in range(layout_container.count()):
            if layout_container.itemAt(i).widget().objectName() == "UpperFrame":
                upper_frame = layout_container.itemAt(i).widget()

        # Get the upper layout by using the name of the class and returning it. Find children returns list so get the
        # single element by using pop
        upper_layout = upper_frame.findChildren(l.UpperLayout, "UpperLayout").pop()

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
