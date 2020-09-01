from PyQt5.QtWidgets import QFrame

# All frames are given their layouts as parameters on creation
class HeadingFrame(QFrame):
    def __init__(self, layout):
        super().__init__()
        self.setObjectName("HeadingFrame")
        self.setLayout(layout)


class StatusFrame(QFrame):
    def __init__(self, layout):
        super().__init__()
        self.setObjectName("StatusFrame")
        self.setLayout(layout)
        # Start the Status Frame Hidden
        self.hide()


class UpperFrame(QFrame):
    def __init__(self, layout):
        super().__init__()
        self.setObjectName("UpperFrame")
        self.setLayout(layout)
