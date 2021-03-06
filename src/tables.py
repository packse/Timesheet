from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView
from PyQt5.QtCore import QTime
from src.pwidgets import BoldTableWidgetItem


class TotalTable(QTableWidget):
    def __init__(self, time_slots):
        super().__init__()


        ##### TEST ZONE ##### ### WHERE WE LEFT OFF ###

        print(time_slots[0].attending_display.start_input.text())
        def time_changed():
            number_am_shift = 0
            number_pm_shift = 0
            number_night_shift = 0
            hrs_am_shift = 0
            hrs_pm_shift = 0
            hrs_night_shift = 0

            for slot in time_slots:
                if slot.option_display.combo_box_widget.currentText() == "Attending Work":
                    start_time_converted = QTime(0, 0, 0).secsTo(slot.attending_display.start_input.time())/60/60
                    if 5 <= start_time_converted <= 10:
                        number_am_shift += 1
                        hrs_am_shift += slot.attending_display.get_time_difference()
                    elif 15 <= start_time_converted <= 17:
                        number_pm_shift += 1
                        hrs_pm_shift += slot.attending_display.get_time_difference()
                    elif 22 <= start_time_converted <= 24 or 0 <= start_time_converted <= 4:
                        ### NEED TO ADD STUFF HERE TO CHECK IF THE CURRENT DATE OF THE SLOT IS FRIDAY OR SUNDAY
                        ### THEREFORE REQUIRING SEPARATION OF WEEKDAY AND WEEKEND

                        number_night_shift += 1
                        hrs_night_shift += slot.attending_display.get_time_difference()

            print(hrs_am_shift)

            #print(time_slots[0].attending_display.start_input.text())

        for slot in time_slots:
            slot.option_display.combo_box_widget.activated.connect(time_changed)
            slot.attending_display.start_input.timeChanged.connect(time_changed)
            slot.attending_display.end_input.timeChanged.connect(time_changed)
            slot.attending_display.break_spinbox.valueChanged.connect(time_changed)

        #time_slots[0].attending_display.start_input.timeChanged.connect(time_changed)



        ##### TEST ZONE #####


        # Stretches the length of the table to fill the space available to it
        horizontal = self.horizontalHeader()
        vertical = self.verticalHeader()
        horizontal.setSectionResizeMode(QHeaderView.Stretch)
        vertical.setSectionResizeMode(QHeaderView.Stretch)

        # Sets the number of rows, columns and removes the headers
        self.setRowCount(3)
        self.setColumnCount(8)
        horizontal.setVisible(False)
        vertical.setVisible(False)

        # Makes the table not editable by the user
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setShowGrid(True)

        self.setItem(1, 0, BoldTableWidgetItem("Number of Hours"))
        self.setItem(2, 0, BoldTableWidgetItem("Number of Shifts"))
        self.setItem(0, 1, BoldTableWidgetItem("AM Weekday"))
        self.setItem(0, 2, BoldTableWidgetItem("PM Weekday"))
        self.setItem(0, 3, BoldTableWidgetItem("Night Shift Weekday"))
        self.setItem(0, 4, BoldTableWidgetItem("AM Weekend"))
        self.setItem(0, 5, BoldTableWidgetItem("PM Weekend"))
        self.setItem(0, 6, BoldTableWidgetItem("Night Shift Weekend"))
        self.setItem(0, 7, BoldTableWidgetItem("Totals"))

        # This will need to take the data in the tab widget and calculate the data from there to create the totals
        self.am_day_hrs = QTableWidgetItem("1,1")
        self.pm_day_hrs = QTableWidgetItem("1,2")
        self.night_day_hrs = QTableWidgetItem("1,3")
        self.am_end_hrs = QTableWidgetItem("1,4")
        self.pm_end_hrs = QTableWidgetItem("1,5")
        self.night_end_hrs = QTableWidgetItem("1,6")
        self.total_hrs = QTableWidgetItem("1,7")

        self.am_day_shifts = QTableWidgetItem("2,1")
        self.pm_day_shifts = QTableWidgetItem("2,2")
        self.night_day_shifts = QTableWidgetItem("2,3")
        self.am_end_shifts = QTableWidgetItem("2,4")
        self.pm_end_shifts = QTableWidgetItem("2,5")
        self.night_end_shifts = QTableWidgetItem("2,6")
        self.total_shifts = QTableWidgetItem("2,7")

        self.setItem(1, 1, self.am_day_hrs)
        self.setItem(1, 2, self.pm_day_hrs)
        self.setItem(1, 3, self.night_day_hrs)
        self.setItem(1, 4, self.am_end_hrs)
        self.setItem(1, 5, self.pm_end_hrs)
        self.setItem(1, 6, self.night_end_hrs)
        self.setItem(1, 7, self.total_hrs)

        self.setItem(2, 1, self.am_day_shifts)
        self.setItem(2, 2, self.pm_day_shifts)
        self.setItem(2, 3, self.night_day_shifts)
        self.setItem(2, 4, self.am_end_shifts)
        self.setItem(2, 5, self.pm_end_shifts)
        self.setItem(2, 6, self.night_end_shifts)
        self.setItem(2, 7, self.total_shifts)



