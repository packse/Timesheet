from src import employee as e
import PyQt5.QtWidgets as qt
from src import layouts as l
from src import savebutton as s

# Displays the label with text 'Name' and allows the user to enter into the text box
def practice_code():
    # Test Data
    emp1 = e.Employee("John", "Nurse")
    # Qapplication required in every qt app. If we had any parameters we would put them in the array
    app = qt.QApplication([])
    # There are a number of different styles that change how the widgets look
    app.setStyle('Fusion')
    # A window contains layouts
    window = qt.QWidget()
    # A layout contains widgets. HBox means Horizontal Box layout in this case
    layout = qt.QHBoxLayout()
    # This creates a label that displays text and cannot be changed by the user directly
    label = qt.QLabel('Name:')
    # This creates an input box for the user to enter text
    name_input = qt.QLineEdit()
    # We can also choose to set the text of the input box ourselves using setText
    name_input.setText(emp1.name)
    # We place our created widgets inside the layout so it can organise how to display it
    layout.addWidget(label)
    # Adding stretch adds an empty box used to separate our widgets and layouts or to push them closer together.
    # It is important to add addStretch() in the right location in code to make it work properly. Think of it like
    # how you would add spacing
    layout.addStretch(0)
    layout.addWidget(name_input)
    # We then set which layout is within that window
    window.setLayout(layout)
    # Displays the layouts within the window. Only need to run it once and not whenever items are updated
    window.show()
    # Executes the application. Make sure to add it to the end of the code
    app.exec_()


# This function writes text to a label with whatever the user enters in the input box by making use of signals
def practice_code2():
    # Just the usual creation of the application, window and layout
    app = qt.QApplication([])
    window = qt.QWidget()
    layout = qt.QHBoxLayout()
    enter = qt.QLineEdit()
    display = qt.QLabel()
    layout.addWidget(enter)
    layout.addWidget(display)
    window.setLayout(layout)
    window.show()


    # The actual function that runs when text has been entered in the input box
    def on_text_entered():
        display.setText(enter.text())

    # The signal here is textChanged which 'signals' when text is changed. The parameter which takes a function is
    # called the slot which in this case is on_text_entered
    enter.textChanged.connect(on_text_entered)

    app.exec_()

def upper_area():
    app = qt.QApplication([])
    app.setStyle('Fusion')
    window = qt.QWidget()
    app.setApplicationName("TimeSheet")
    vertical_layout_container = qt.QVBoxLayout()
    upper_layout = l.UpperLayout()
    vertical_layout_container.addLayout(l.HeadingLayout())
    vertical_layout_container.addLayout(l.StatusLayout())
    vertical_layout_container.addLayout(upper_layout)
    frame = qt.QFrame()
    window.setLayout(vertical_layout_container)
    upper_layout.addWidget(s.SaveButton(vertical_layout_container))
    window.show()
    app.exec_()

if __name__ == '__main__':

    upper_area()

