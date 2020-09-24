from PyQt5.QtWidgets import QPushButton, QVBoxLayout
from src import employee as e
from PyQt5.QtCore import QSettings
from src import layouts as l
from src import frames as f


# Button that saves all data including employee details and current timesheet data
class SaveButton(QPushButton):
    # Parameter includes the main container that holds all other layouts
    def __init__(self, layout_container: QVBoxLayout):
        super().__init__()
        self.setText('Save')
        # The location that the save button will save the details section (name, classification) information in
        settings = QSettings('Noone', 'TimeSheet')

        # QVBoxLayout is only sent due to UpperFrame needing a class to initialise
        # We get object name by creating a dummy frame object in order to return the name
        details_frame = get_frame(layout_container, f.DetailsFrame(QVBoxLayout()).objectName())
        status_frame = get_frame(layout_container, f.StatusFrame(QVBoxLayout()).objectName())
        time_frame = get_frame(layout_container, f.TimePeriodFrame(QVBoxLayout()).objectName())

        # Get the upper and status layout by using the objectName of the class and returning it.
        # Find children returns a list so to get the single element we use pop()
        details_layout = details_frame.findChildren(l.DetailsLayout, l.DetailsLayout().objectName()).pop()
        status_layout = status_frame.findChildren(l.StatusLayout, l.StatusLayout().objectName()).pop()
        time_layout = time_frame.findChildren(l.TimePeriodLayout, l.TimePeriodLayout().objectName()).pop()

        # Saves the specified details when the button is clicked
        def save_button_clicked():
            status_frame.show()
            # Get the name and classification text for the input box
            name_text = details_layout.name_input.text()
            class_text = details_layout.classification_input.text()
            # Create an employee object from that text to set it properly
            temp = e.Employee(name_text, class_text)

            error_message = ""

            if temp.name == "":
                error_message += "- Please enter a valid name\n"
            if temp.classification == "":
                error_message += "- Please enter a valid classification\n"

            if error_message == "":
                settings.setValue('Name text', temp.name)
                settings.setValue('Classification text', temp.classification)
                settings.setValue('Start date', time_layout.start_date.text())
                status_layout.head_label.setText("Success!")
                status_layout.body_label.setText("Save was successful")
            else:
                status_layout.head_label.setText("Error")
                status_layout.body_label.setText(error_message)

        # When the save button is clicked run the save_button_clicked function
        self.clicked.connect(save_button_clicked)


# Helper function to return the frame using the name of the frame we are looking for
def get_frame(layout_container, name):
    for i in range(layout_container.count()):
        current_frame = layout_container.itemAt(i).widget()
        if current_frame.objectName() == name:
            return current_frame