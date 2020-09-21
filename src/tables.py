from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView


class TotalTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setRowCount(3)
        self.setColumnCount(6)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setShowGrid(True)

        self.setItem(1, 0, QTableWidgetItem("Number of Hours"))
        self.setItem(2, 0, QTableWidgetItem("Number of Shifts"))
        self.setItem(0, 1, QTableWidgetItem("AM Weekday"))
        self.setItem(0, 2, QTableWidgetItem("PM Weekday"))
        self.setItem(0, 3, QTableWidgetItem("AM Weekend"))
        self.setItem(0, 4, QTableWidgetItem("PM Weekend"))
        self.setItem(0, 5, QTableWidgetItem("Totals"))

        # This will need to take the data in the tab widget and calculate the data from there to create the totals
        self.am_day_hrs = QTableWidgetItem("1,1")
        self.pm_day_hrs = QTableWidgetItem("1,2")
        self.am_end_hrs = QTableWidgetItem("1,3")
        self.pm_end_hrs = QTableWidgetItem("1,4")
        self.total_hrs = QTableWidgetItem("1,5")

        self.am_day_shifts = QTableWidgetItem("2,1")
        self.pm_day_shifts = QTableWidgetItem("2,2")
        self.am_end_shifts = QTableWidgetItem("2,3")
        self.pm_end_shifts = QTableWidgetItem("2,4")
        self.total_shifts = QTableWidgetItem("2,5")

        self.setItem(1, 1, self.am_day_hrs)
        self.setItem(1, 2, self.pm_day_hrs)
        self.setItem(1, 3, self.am_end_hrs)
        self.setItem(1, 4, self.pm_end_hrs)
        self.setItem(1, 5, self.total_hrs)

        self.setItem(2, 1, self.am_day_shifts)
        self.setItem(2, 2, self.pm_day_shifts)
        self.setItem(2, 3, self.am_end_shifts)
        self.setItem(2, 4, self.pm_end_shifts)
        self.setItem(2, 5, self.total_shifts)


