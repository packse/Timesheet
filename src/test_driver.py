from src import employee as e
import PyQt5.QtWidgets as qt
from src import layouts as l
from src import savebutton as s
from src import frames as f
from src import pages as p
from src import tables as t
import PyQt5.QtGui

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
    # This adds margins around the layout to provide it with additional space
    layout.setContentsMargins(0,0,0,0)
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

def test_zone():
    app = qt.QApplication([])
    app.setStyle('Fusion')
    app.setApplicationName("TimeSheet")
    main_window = qt.QWidget()
    vertical_layout_container = qt.QVBoxLayout()
    main_window.setLayout(vertical_layout_container)

    details_layout = l.DetailsLayout()

    heading_frame = f.HeadingFrame(l.HeadingLayout())
    status_frame = f.StatusFrame(l.StatusLayout())
    details_frame = f.DetailsFrame(details_layout)

    vertical_layout_container.addWidget(heading_frame)
    vertical_layout_container.addWidget(status_frame)
    vertical_layout_container.addWidget(details_frame)
    details_layout.addWidget(s.SaveButton(vertical_layout_container))


    main_window.show()
    app.exec_()


def grid_layout_practice():
    app = qt.QApplication([])
    app.setStyle('Fusion')
    app.setApplicationName("TimeSheet")

    main_window = qt.QWidget()
    layout = qt.QGridLayout(main_window)

    layout.addWidget(qt.QLabel("Number of Hours"), 1, 0)
    layout.addWidget(qt.QLabel("Number of Shifts"), 2, 0)
    layout.addWidget(qt.QLabel("AM Weekday"), 0, 1)
    layout.addWidget(qt.QLabel("PM Weekday"), 0, 2)
    layout.addWidget(qt.QLabel("AM Weekend"), 0, 3)
    layout.addWidget(qt.QLabel("PM Weekend"), 0, 4)
    layout.addWidget(qt.QLabel("Totals"), 0, 5)
    layout.addWidget(qt.QLabel("S"), 1, 1)
    layout.addWidget(qt.QLabel("S"), 1, 2)
    layout.addWidget(qt.QLabel("S"), 1, 3)
    layout.addWidget(qt.QLabel("S"), 1, 4)
    layout.addWidget(qt.QLabel("S"), 1, 5)
    layout.addWidget(qt.QLabel("S"), 2, 1)
    layout.addWidget(qt.QLabel("S"), 2, 2)
    layout.addWidget(qt.QLabel("S"), 2, 3)
    layout.addWidget(qt.QLabel("S"), 2, 4)
    layout.addWidget(qt.QLabel("S"), 2, 5)

    main_window.show()
    app.exec_()

def test_zone2():
    app = qt.QApplication([])
    app.setStyle('Fusion')
    app.setApplicationName("TimeSheet")

    main_window = qt.QWidget()
    layout = qt.QHBoxLayout(main_window)
    table_widget = t.TotalTable()

    layout.addWidget(table_widget)







    main_window.show()
    app.exec_()

def scroll_area_practice():
    app = qt.QApplication([])
    app.setStyle('Fusion')
    app.setApplicationName("TimeSheet")


    main_window = qt.QWidget()
    tab_widget = qt.QTabWidget()
    scroll_widget = qt.QScrollArea()
    scroll_widget2 = qt.QScrollArea()

    # By putting the widget in the brackets you automatically set the widgets layout without having to call setLayout()
    main_layout = qt.QVBoxLayout(main_window)
    # Adds the tab widget to the main window widget. It will be added the same in our case except to vertical container
    main_layout.addWidget(tab_widget)

    # Creates a new tab page which will contain our scrollArea widget
    tab_widget.addTab(scroll_widget, "TAB 1")
    tab_widget.addTab(scroll_widget2, "TAB 2")

    # Scroll area requires an inner content widget to hold data since it is technically only a container.
    # Otherwise scrolling doesn't work properly
    inner_widget = qt.QWidget()
    inner_widget2 = qt.QWidget()
    # Here we reduce by a line of code by setting which widget this layout belongs to
    scroll_layout = qt.QVBoxLayout(inner_widget)
    scroll_layout2 = qt.QVBoxLayout(inner_widget2)
    test_label = qt.QLabel("WORDS AND LOTS OF EM FDHBHJDFBHDSBFJ")
    test_label2 = qt.QLabel("A SECOND TAB OF WORDS AND LOTS OF EM")
    scroll_layout.addWidget(test_label)
    scroll_layout2.addWidget(test_label2)
    # Important: setWidget can only be called after our inner content widget has been created and populated otherwise
    # the data will not display. If necessary this can be fixed by using setWidgetResizable(True)
    scroll_widget.setWidget(inner_widget)
    scroll_widget2.setWidget(inner_widget2)


    main_window.show()
    app.exec_()


def stacked_container_practice():
    app = qt.QApplication([])
    app.setStyle('Fusion')
    app.setApplicationName("TimeSheet")


    # Create the widgets
    main_window = qt.QWidget()
    stacked_widget = qt.QStackedWidget()
    # First and second page widgets for the stacked layouts are created
    first_page_widget = qt.QWidget()
    second_page_widget = qt.QWidget()

    # Shows the current index of the stacked widget that is being displayed
    def show_index():
        print(stacked_widget.currentIndex())

    # Set the layouts of all of the widgets
    main_window_layout = qt.QHBoxLayout(main_window)
    first_page_layout = qt.QVBoxLayout(first_page_widget)
    second_page_layout = qt.QVBoxLayout(second_page_widget)

    # Creates the combobox. Each combobox has an index that can be retrieved starting from 0
    page_combo_box = qt.QComboBox()
    page_combo_box.addItem("PAGE1")
    page_combo_box.addItem("PAGE2")

    # I assume that activated holds the index of the option that was selected and then sends it to the stacked widget to
    # set which index that will be displayed. Otherwise it just uses some kind of black magic
    page_combo_box.activated.connect(stacked_widget.setCurrentIndex)
    page_combo_box.activated.connect(show_index)

    # Adds the test text to the page layouts
    first_page_layout.addWidget(qt.QLabel("WORDS"))
    first_page_layout.addWidget(qt.QLabel("AND"))
    first_page_layout.addWidget(qt.QLabel("MORE"))
    first_page_layout.addWidget(qt.QLabel("WORDS"))
    second_page_layout.addWidget(qt.QLabel("LOTS"))
    second_page_layout.addWidget(qt.QLabel("AND"))
    second_page_layout.addWidget(qt.QLabel("LOTS"))

    # Adds the page widgets to the stacked widget
    stacked_widget.addWidget(first_page_widget)
    stacked_widget.addWidget(second_page_widget)

    # Adds the combo box and stacked layout to the main window
    main_window_layout.addWidget(page_combo_box)
    main_window_layout.addWidget(stacked_widget)
    main_window_layout.addStretch()


    main_window.show()
    app.exec_()







if __name__ == '__main__':

    test_zone2()

