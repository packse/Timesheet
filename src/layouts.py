from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QDateEdit
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSettings, QDate


# The top heading section of the application
class HeadingLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.setObjectName("HeadingLayout")

        heading_label = QLabel("Timesheet Program")
        heading_label.setAlignment(Qt.AlignCenter)
        self.addWidget(heading_label)


# The status message section that alerts the user to any errors or successes particularly when saving data
class StatusLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.setObjectName("StatusLayout")

        self.head_label = QLabel()
        self.head_label.setAlignment(Qt.AlignCenter)
        self.body_label = QLabel()
        self.addWidget(self.head_label)
        self.addWidget(self.body_label)

# The section for users to enter their name and classification
class DetailsLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.setObjectName("DetailsLayout")
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


# Section to enter the start date of the fortnight
class TimePeriodLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.setObjectName("TimePeriodLayout")

        self.start_label = QLabel("Start Date")
        self.start_date = QDateEdit()
        self.start_date.setCalendarPopup(True)
        # Can choose a start date from a fortnight (-14) before current date
        self.start_date.setMinimumDate(QDate().currentDate().addDays(-14))
        self.start_date.setMaximumDate(QDate().currentDate())
        self.end_label = QLabel("End Date")
        self.end_date = QDateEdit()
        self.end_date.setDate(self.start_date.date().addDays(14))
        # (2) removes the arrow from the QDate edit
        self.end_date.setButtonSymbols(2)
        self.end_date.setReadOnly(True)

        self.addWidget(self.start_label)
        self.addWidget(self.start_date)
        self.addWidget(self.end_label)
        self.addWidget(self.end_date)

        # Whenever the start date is changed make the end date a fortnight past the new start date
        def set_end_date():
            new_date = self.start_date.date()
            self.end_date.setDate(new_date.addDays(14))

        self.start_date.dateChanged.connect(set_end_date)
