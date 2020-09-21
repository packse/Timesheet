from PyQt5.QtWidgets import QFrame


# All frames are given their layouts as parameters on creation
# QFrames operate identical to normal QWidgets with the added capability to add borders
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


class DetailsFrame(QFrame):
    def __init__(self, layout):
        super().__init__()
        self.setObjectName("DetailsFrame")
        self.setLayout(layout)


class TimePeriodFrame(QFrame):
    def __init__(self, layout):
        super().__init__()
        self.setObjectName("TimePeriodFrame")
        self.setLayout(layout)


class TimeTabFrame(QFrame):
    def __init__(self, layout):
        super().__init__()
        self.setObjectName("TimeTabFrame")
        self.setLayout(layout)


class TotalsTableFrame(QFrame):
    def __init__(self, layout):
        super().__init__()
        self.setObjectName("TotalsTableFrame")
        self.setLayout(layout)