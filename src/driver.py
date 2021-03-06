from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication
from src import layouts as l
from src import frames as f
from src import savebutton as s
from src import pages as p


# Window widget that contains all other widgets and layouts within it
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Vertical layout that contains all other layouts and widgets within it
        vertical_layout_container = QVBoxLayout(self)

        # Initialised early because its needed for both adding it to the frame widget and adding save button to it
        details_layout = l.DetailsLayout()

        # Creates the frames and the layouts. The layouts contain other widgets within them.
        heading_frame = f.HeadingFrame(l.HeadingLayout())
        status_frame = f.StatusFrame(l.StatusLayout())
        details_frame = f.DetailsFrame(details_layout)
        time_period_frame = f.TimePeriodFrame(l.TimePeriodLayout())
        time_tab_frame = p.TimeSlotContainer(time_period_frame.layout().start_date)
        # Need to send through array of timeslots for table to work with when spinboxes are changed
        totals_table_frame = f.TotalsTableFrame(l.TotalsTableLayout(time_tab_frame.timeslot_row_arr))

        # Adds the widgets to the vertical layout container for the main screen.
        vertical_layout_container.addWidget(heading_frame)
        vertical_layout_container.addWidget(status_frame)
        vertical_layout_container.addWidget(details_frame)
        vertical_layout_container.addWidget(time_period_frame)
        vertical_layout_container.addWidget(time_tab_frame)
        vertical_layout_container.addWidget(totals_table_frame)

        # Save button placed at the end once all other layouts have been initialised
        details_layout.addWidget(s.SaveButton(vertical_layout_container))

        self.show()


# QApplication object that creates the actual application instance
class App(QApplication):
    def __init__(self):
        super().__init__([])
        self.setStyle('Fusion')
        self.setApplicationName("TimeSheet")


if __name__ == '__main__':
    app = App()
    main_window = MainWindow()
    # Put at the end of all code to start executing the created application
    app.exec_()

