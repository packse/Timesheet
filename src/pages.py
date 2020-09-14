# Contains the pages that will be within for the stacked layout
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QDoubleSpinBox, QCheckBox, QTimeEdit
from PyQt5.QtCore import Qt


# Might need to consider using grid layout to layout it out properly. Could also try to use stretch or margins or size policy

# Widget that contains only the date and the options to select which page to show for the stacked layout
class OptionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        self.start_date_layout = QVBoxLayout()
        self.option_layout = QVBoxLayout()

        self.start_date_headlabel = QLabel("Start Date:")
        # Right now this is a placeholder value but it will need to be sent in through the constructor
        self.start_date_label = QLabel("Friday 10/3/20")

        self.combo_box_widget = QComboBox()
        self.combo_box_widget.addItem("Attending Work")
        self.combo_box_widget.addItem("Sick Day")
        self.combo_box_widget.addItem("Annual Leave")
        self.combo_box_widget.addItem("Training Only")

        self.option_layout.addWidget(self.combo_box_widget)

        self.start_date_layout.addWidget(self.start_date_headlabel)
        self.start_date_layout.addStretch(1)
        self.start_date_layout.addWidget(self.start_date_label)

        self.layout.addLayout(self.start_date_layout)
        self.layout.addLayout(self.option_layout)




class AttendingPg(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)

        self.start_layout = QVBoxLayout()
        self.start_label = QLabel("Start Time:")
        self.start_input = QTimeEdit()
        self.start_input.setDisplayFormat("HH:mm")

        self.end_layout = QVBoxLayout()
        self.end_label = QLabel("End Time:")
        self.end_input = QTimeEdit()
        self.end_input.setDisplayFormat("HH:mm")

        self.break_layout = QVBoxLayout()
        self.break_label = QLabel("Break (Hrs)")
        self.break_spinbox = QDoubleSpinBox()
        self.break_spinbox.setSingleStep(.5)

        self.holiday_layout = QVBoxLayout()
        self.holiday_label = QLabel("Public Holiday:")
        self.holiday_checkbox_1 = QCheckBox("Friday 10/3/20")
        self.holiday_checkbox_2 = QCheckBox("Saturday 11/3/20")
        # Starts disabled but can be enabled if the user works until the next day
        self.holiday_checkbox_2.setEnabled(False)

        self.training_layout = QVBoxLayout()
        self.training_label = QLabel("Training (Hrs)")
        self.training_spinbox = QDoubleSpinBox()
        self.training_spinbox.setSingleStep(.5)

        # Changed programmatically based on data entered in start and end inputs
        self.info_layout = QVBoxLayout()
        self.info_heading_label = QLabel("Hours Calculated:")
        self.info_normal_label = QLabel("Normal Day Hours: 0")
        self.info_holiday_label = QLabel("Public Holiday Hours: 0")


        self.layout.addLayout(self.start_layout)
        self.start_layout.addWidget(self.start_label)
        self.start_layout.addStretch(1)
        self.start_layout.addWidget(self.start_input)

        self.layout.addLayout(self.end_layout)
        self.end_layout.addWidget(self.end_label)
        self.end_layout.addStretch(1)
        self.end_layout.addWidget(self.end_input)

        self.layout.addLayout(self.break_layout)
        self.break_layout.addWidget(self.break_label)
        self.break_layout.addStretch(1)
        self.break_layout.addWidget(self.break_spinbox)

        self.layout.addLayout(self.holiday_layout)
        self.holiday_layout.addWidget(self.holiday_label)
        self.holiday_layout.addStretch(1)
        self.holiday_layout.addWidget(self.holiday_checkbox_1)
        self.holiday_layout.addWidget(self.holiday_checkbox_2)

        self.layout.addLayout(self.training_layout)
        self.training_layout.addWidget(self.training_label)
        self.training_layout.addStretch(1)
        self.training_layout.addWidget(self.training_spinbox)

        self.layout.addLayout(self.info_layout)
        self.info_layout.addWidget(self.info_heading_label)
        self.info_layout.addStretch(1)
        self.info_layout.addWidget(self.info_normal_label)
        self.info_layout.addWidget(self.info_holiday_label)



class SickDayPg(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)

        self.hrs_layout = QVBoxLayout()
        self.hrs_label = QLabel("Sick Leave Hours:")
        self.hrs_spinbox = QDoubleSpinBox()
        self.hrs_spinbox.setSingleStep(.5)

        self.certificate_layout = QVBoxLayout()
        self.certificate_label = QLabel("Have Certificate")
        self.certificate_checkbox = QCheckBox()

        self.layout.addLayout(self.hrs_layout)
        self.hrs_layout.addWidget(self.hrs_label)
        self.hrs_layout.addStretch(1)
        self.hrs_layout.addWidget(self.hrs_spinbox)

        self.layout.addLayout(self.certificate_layout)
        self.certificate_layout.addWidget(self.certificate_label)
        self.certificate_layout.addStretch(1)
        self.certificate_layout.addWidget(self.certificate_checkbox)


class AnnualLeavePg(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)

        self.hrs_layout = QVBoxLayout()
        self.hrs_label = QLabel("Annual Hours:")
        self.hrs_spinbox = QDoubleSpinBox()
        self.hrs_spinbox.setSingleStep(.5)

        self.layout.addLayout(self.hrs_layout)
        self.hrs_layout.addWidget(self.hrs_label)
        self.hrs_layout.addStretch(1)
        self.hrs_layout.addWidget(self.hrs_spinbox)




class TrainingOnlyPg(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)

        self.hrs_layout = QVBoxLayout()
        self.hrs_label = QLabel("Training Hours:")
        self.hrs_spinbox = QDoubleSpinBox()
        self.hrs_spinbox.setSingleStep(.5)

        # Training_hrs_layout is made a child layout of the main layout. Consider putting this layout in its own widget
        # first if that makes it easier to access the data within it
        self.layout.addLayout(self.hrs_layout)
        self.hrs_layout.addWidget(self.hrs_label)
        self.hrs_layout.addStretch(1)
        self.hrs_layout.addWidget(self.hrs_spinbox)





