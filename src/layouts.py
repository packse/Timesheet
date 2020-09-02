from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSettings

# The top heading section of the application
class HeadingLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        heading_label = QLabel("Timesheet Program")
        heading_label.setAlignment(Qt.AlignCenter)
        self.addWidget(heading_label)

        self.setObjectName("HeadingLayout")


# The status message section that alerts the user to any errors or successes particularly when saving data
class StatusLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.head_label = QLabel()
        self.head_label.setAlignment(Qt.AlignCenter)
        self.body_label = QLabel()
        self.addWidget(self.head_label)
        self.addWidget(self.body_label)

        self.setObjectName("StatusLayout")


class DetailsLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        # Receives any existing data for the details section (name, classification)
        settings = QSettings('Noone', 'TimeSheet')

        self.name_label = QLabel('Employee:')
        self.name_input = QLineEdit(settings.value('Name text'))
        # Max character length
        self.name_input.setMaxLength(50)
        self.classification_label = QLabel('Classification:')
        self.classification_input = QLineEdit(settings.value('Classification text'))
        self.classification_input.setMaxLength(30)
        self.addWidget(self.name_label)
        self.addWidget(self.name_input)
        self.addWidget(self.classification_label)
        self.addWidget(self.classification_input)

        self.setObjectName("DetailsLayout")



