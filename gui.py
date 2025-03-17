from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QSpinBox, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from logic import schedule_shutdown, cancel_shutdown

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shutdown Timer")
        self.setGeometry(400, 200, 300, 200)
        
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Shutdown in (minutes):", self)
        layout.addWidget(self.label)

        self.time_input = QSpinBox(self)
        self.time_input.setRange(1, 1440)
        self.time_input.setValue(10)
        layout.addWidget(self.time_input)

        self.start_button = QPushButton("Start the timer", self)
        self.start_button.clicked.connect(self.start_timer)
        layout.addWidget(self.start_button)

        self.cancel_button = QPushButton("Cancel the timer", self)
        self.cancel_button.clicked.connect(self.cancel_timer)
        layout.addWidget(self.cancel_button)

        self.timer_label = QLabel("", self)
        layout.addWidget(self.timer_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.seconds_left = 0

    def start_timer(self):
        minutes = self.time_input.value()
        self.seconds_left = minutes * 60
        self.timer.start(1000)
        schedule_shutdown(minutes)

    def update_timer(self):
        if self.seconds_left > 0:
            minutes_left, seconds = divmod(self.seconds_left, 60)
            self.timer_label.setText(f'Time is running out: {minutes_left:02}:{seconds:02}')
            self.seconds_left -= 1
        else:
            self.timer.stop()
            self.timer_label.setText('Turning off...')

    def cancel_timer(self):
        self.timer.stop()
        self.timer_label.setText('')
        cancel_shutdown()