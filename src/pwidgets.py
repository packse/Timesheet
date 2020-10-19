# Widgets that have had their classes and functions edited. The P in Pwidgets denotes Personal #
from PyQt5.QtWidgets import QDoubleSpinBox, QTimeEdit, QComboBox, QTableWidgetItem
from PyQt5.QtGui import QFont


# Ignores the wheel event that would normally change the values in the spinbox
class PDoubleSpinBox(QDoubleSpinBox):
    def wheelEvent(self, event):
        event.ignore()


class PTimeEdit(QTimeEdit):
    def wheelEvent(self, event):
        event.ignore()

    # Increases/Decreases by 15 when pressing the up down key in timeedit in minutes
    def stepBy(self, steps):
        if self.currentSection() == self.MinuteSection:
            QTimeEdit.stepBy(self, steps * 15)
        else:
            QTimeEdit.stepBy(self, steps)


class PComboBox(QComboBox):
    def wheelEvent(self, event):
        event.ignore()


# Sets the table headings font to bold
class BoldTableWidgetItem(QTableWidgetItem):
    def __init__(self, text=""):
        super().__init__()
        bold_font = QFont("Helvetica", 10, QFont.Bold)
        self.setText(text)
        self.setFont(bold_font)