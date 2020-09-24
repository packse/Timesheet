# Contains the widgets that that will be used for the middle section #
from PyQt5.QtWidgets import QWidget, QFrame, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QDoubleSpinBox, QCheckBox, \
                                            QTimeEdit, QStackedWidget, QTabWidget, QScrollArea
from src import helper as h
from PyQt5.QtCore import QTime

# Contains two weeks worth of timeslots with a tab for the first and second week
class TimeSlotContainer(QTabWidget):
    def __init__(self, date_edit):
        super().__init__()
        num_days = 14
        # For week 1 of a fortnight
        self.scroll_area1 = QScrollArea()
        self.scroll_window1 = QWidget()
        self.scroll_window_layout1 = QVBoxLayout(self.scroll_window1)

        # For week 2 of a fortnight
        self.scroll_area2 = QScrollArea()
        self.scroll_window2 = QWidget()
        self.scroll_window_layout2 = QVBoxLayout(self.scroll_window2)

        # Stores the timeslots for each day within an array
        self.timeslot_row_arr = []
        # Sets the start date as the date retrieved as a parameter from the time period section
        date = date_edit.date()

        # Creates timeslot rows for as many days specified in num_days and adds them to the array and tabs
        for i in range(num_days):
            current_row = TimeSlotRow(date.addDays(i))
            if i < num_days/2:
                self.scroll_window_layout1.addWidget(current_row)
            else:
                self.scroll_window_layout2.addWidget(current_row)
            self.timeslot_row_arr.append(current_row)

        # When the start date is changed then update the start_date_label variable for the timeslot object to the new
        # date range
        def start_date_changed():
            new_date = date_edit.date()
            if self.timeslot_row_arr is not None:
                for ii in range(num_days):
                    self.timeslot_row_arr[ii].option_display.start_date_label.setText\
                        (h.format_qdate(new_date.addDays(ii)))

        date_edit.dateChanged.connect(start_date_changed)

        self.addTab(self.scroll_area1, "Week 1")
        self.addTab(self.scroll_area2, "Week 2")

        # Need it to be resizable otherwise it doesn't resize when the screen size is increased
        self.scroll_area1.setWidgetResizable(True)
        self.scroll_area1.setWidget(self.scroll_window1)

        self.scroll_area2.setWidgetResizable(True)
        self.scroll_area2.setWidget(self.scroll_window2)


# Holds the optionWidget and stackedLayout pages in a single frame
class TimeSlotRow(QFrame):
    def __init__(self, date):
        super().__init__()
        self.layout = QHBoxLayout(self)
        # Sets the style of the lines drawn. Check online QFrame for more options
        self.setLineWidth(1)
        self.setFrameShape(QFrame.Plain | QFrame.Box)

        # Creates the different displays for the stacked widget.
        self.option_display = OptionWidget(date)
        self.attending_display = AttendingPg()
        self.sick_leave_display = SickDayPg()
        self.annual_leave_display = AnnualLeavePg()
        self.training_display = TrainingOnlyPg()
        self.not_working_display = NotWorkingPg()

        # Adds these displays to the stacked widget
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.attending_display)
        self.stacked_widget.addWidget(self.sick_leave_display)
        self.stacked_widget.addWidget(self.annual_leave_display)
        self.stacked_widget.addWidget(self.training_display)
        self.stacked_widget.addWidget(self.not_working_display)

        # When the combo box is changed then change to the relevant stacked layout
        self.option_display.combo_box_widget.activated.connect(self.stacked_widget.setCurrentIndex)

        self.layout.addWidget(self.option_display)
        self.layout.addWidget(self.stacked_widget)


# Widget that contains the date and the combo box to select which page to show for the stacked layout
class OptionWidget(QWidget):
    def __init__(self, date):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        self.start_date_layout = QVBoxLayout()
        self.option_layout = QVBoxLayout()

        # Creates the start date label that displays the date of that timeslot
        self.start_date_headlabel = QLabel("Start Date:")
        self.start_date_label = QLabel(h.format_qdate(date))

        # Create the combo box and the items within it
        self.combo_box_widget = QComboBox()
        self.combo_box_widget.addItem("Attending Work")
        self.combo_box_widget.addItem("Sick Day")
        self.combo_box_widget.addItem("Annual Leave")
        self.combo_box_widget.addItem("Training Only")
        self.combo_box_widget.addItem("Not Working")

        self.option_layout.addWidget(self.combo_box_widget)

        self.start_date_layout.addWidget(self.start_date_headlabel)
        self.start_date_layout.addStretch(1)
        self.start_date_layout.addWidget(self.start_date_label)

        self.layout.addLayout(self.start_date_layout)
        self.layout.addLayout(self.option_layout)

# Option for when the employee is attending work and needs to fill in their work hours
class AttendingPg(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)

        # Creating the layouts #
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
        # Starts disabled but can turn enabled if the user works until the next day
        self.holiday_checkbox_2.setEnabled(False)

        self.training_layout = QVBoxLayout()
        self.training_label = QLabel("Training (Hrs)")
        self.training_spinbox = QDoubleSpinBox()
        self.training_spinbox.setSingleStep(.5)

        # Changed programmatically based on data entered in start and end inputs
        self.info_layout = QVBoxLayout()
        self.info_heading_label = QLabel("Hours Calculated:")
        self.info_normal_label = QLabel("Normal Day Hours: " +
                                        str(self.get_time_difference()))
        # We don't save the status of the  public holidays checkbox so we set it to 0 on startup
        self.info_holiday_label = QLabel("Public Holiday Hours: 0.0")

        # When either the start or finish time is changed by the user
        def time_changed():
            # If the start time is larger than end time then it means work hours extend to the next day
            if self.start_input.time() > self.end_input.time():
                self.holiday_checkbox_2.setEnabled(True)
            # If it is smaller than disable and uncheck the next day checkbox
            else:
                self.holiday_checkbox_2.setEnabled(False)
                self.holiday_checkbox_2.setChecked(False)
            # Calculate the difference between start and end time
            difference = self.get_time_difference()
            # Calculate the hours using the difference and display them hrs
            self.calculate_hrs(difference)

        self.start_input.timeChanged.connect(time_changed)
        self.end_input.timeChanged.connect(time_changed)
        self.break_spinbox.valueChanged.connect(time_changed)

        # If a public holiday checkbox is changed then calculate the hours to display
        def checkbox_changed():
            difference = self.get_time_difference()
            self.calculate_hrs(difference)

        self.holiday_checkbox_1.stateChanged.connect(checkbox_changed)
        self.holiday_checkbox_2.stateChanged.connect(checkbox_changed)

        # Adding the Layouts #

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

    # Uses the start and end inputs and then returns the difference in hours between them
    def get_time_difference(self):
        start_time = self.start_input.time()
        end_time = self.end_input.time()
        # Convert difference in seconds to hours
        difference = start_time.secsTo(end_time) / 60 / 60
        # If difference is negative then subtract it from 24 hours to wrap around
        if difference < 0:
            # + because using - would cancel out the operation turning it to addition
            difference = 24 + difference

        return difference

    # Calculates the hours for normal and public holidays and displays them in their label
    def calculate_hrs(self, difference):
        # Calculations from start time to midnight and midnight to end time
        start_to_mid_hrs = QTime(0, 0).secsTo(self.end_input.time()) / 60 / 60
        mid_to_end_hrs = 24 - (QTime(0, 0).secsTo(self.start_input.time()) / 60 / 60)
        # Set difference to total hours - break time
        difference -= self.break_spinbox.value()

        # If both holiday checkbox 1 and 2 are checked or only checkbox 1 can be and is checked then display difference
        # in public holiday hrs
        if self.holiday_checkbox_1.isChecked() and (self.holiday_checkbox_2.isChecked() or
                                                    not self.holiday_checkbox_2.isEnabled()):
            self.info_normal_label.setText("Normal Day Hours: 0.0")
            self.info_holiday_label.setText("Public Holiday Hours: " + str(difference))

        # If neither checkbox 1 or 2 are checked then display the difference in normal hrs
        elif not self.holiday_checkbox_1.isChecked() and not self.holiday_checkbox_2.isChecked():
            self.info_normal_label.setText("Normal Day Hours: " + str(difference))
            self.info_holiday_label.setText("Public Holiday Hours: 0.0")

        # If checkbox 1 is checked and checkbox 2 can be checked but is not then take the hours from the first day
        # for public holiday hrs and the remainder for normal hours
        elif self.holiday_checkbox_1.isChecked() and (self.holiday_checkbox_2.isEnabled()
                                                      and not self.holiday_checkbox_2.isChecked()):
            start_to_mid_hrs -= self.break_spinbox.value()
            self.info_normal_label.setText("Normal Day Hours: " + str(start_to_mid_hrs))
            self.info_holiday_label.setText("Public Holiday Hours: " + str(mid_to_end_hrs))

        # If checkbox 2 is checked but checkbox 1 isn't then take the hours from the second day for public holiday
        # hrs and the rest for normal hours
        elif self.holiday_checkbox_2.isChecked() and (self.holiday_checkbox_1.isEnabled()
                                                      and not self.holiday_checkbox_1.isChecked()):
            # break time reduces from normal day hours rather than holiday hours
            mid_to_end_hrs -= self.break_spinbox.value()
            self.info_normal_label.setText("Normal Day Hours: " + str(mid_to_end_hrs))
            self.info_holiday_label.setText("Public Holiday Hours: " + str(start_to_mid_hrs))


# When the employee needs to fill in a sick day
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

        # If the employee has a certificate then they can choose to tick the box
        self.layout.addLayout(self.certificate_layout)
        self.certificate_layout.addWidget(self.certificate_label)
        self.certificate_layout.addStretch(1)
        self.certificate_layout.addWidget(self.certificate_checkbox)


# For when the employee is away or on annual leave
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

# For when the employee only comes in for work for training
class TrainingOnlyPg(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)

        self.hrs_layout = QVBoxLayout()
        self.hrs_label = QLabel("Training Hours:")
        self.hrs_spinbox = QDoubleSpinBox()
        self.hrs_spinbox.setSingleStep(.5)

        self.layout.addLayout(self.hrs_layout)
        self.hrs_layout.addWidget(self.hrs_label)
        self.hrs_layout.addStretch(1)
        self.hrs_layout.addWidget(self.hrs_spinbox)


# For when the employee is not scheduled to work on that day
class NotWorkingPg(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
