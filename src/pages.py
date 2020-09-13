# Contains the pages that will be within for the stacked layout

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QDoubleSpinBox


# Widget that contains only the date and the options to select which page to show for the stacked layout
class OptionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        self.start_date_widget = QWidget()
        self.start_date_layout = QVBoxLayout(self.start_date_widget)
        self.start_date_headlabel = QLabel("Start Date:")
        # Right now this is a placeholder value but it will need to be sent in through the constructor
        self.start_date_label = QLabel("10/3/20")
        self.combo_box_widget = QComboBox()
        self.combo_box_widget.addItem("Attending Work")
        self.combo_box_widget.addItem("Sick Day")
        self.combo_box_widget.addItem("Annual Leave")
        self.combo_box_widget.addItem("Training Only")


        self.start_date_layout.addWidget(self.start_date_headlabel)
        self.start_date_layout.addWidget(self.start_date_label)
        self.layout.addWidget(self.start_date_widget)
        self.layout.addWidget(self.combo_box_widget)




class AttendingPg(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel("WORSDSDADJFBHDGBJ"))


class SickDayPg(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel("FDGDGGDSGDS"))


class AnnualLeavePg(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel("DFFDF"))




class TrainingOnlyPg(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.training_label = QLabel("Training Hours:")
        self.training_spinbox = QDoubleSpinBox()
        self.training_spinbox.setSingleStep(.5)
        self.layout.addWidget(self.training_label)
        self.layout.addWidget(self.training_spinbox)





