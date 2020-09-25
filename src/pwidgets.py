# Widgets that have had their classes and functions edited. The P in Pwidgets denotes Personal #
from PyQt5.QtWidgets import QDoubleSpinBox, QTimeEdit, QComboBox


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

