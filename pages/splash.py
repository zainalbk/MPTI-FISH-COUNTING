"""
BACKUP ORIGINAL SPLASH CODE:
Splash screen dengan dark theme, logo "S", progress bar animasi.
File: pages/splash.py (original version)
"""

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar
from PyQt5.QtGui import QFont, QPixmap
from widgets.reference_ui import FishLogo
import os


class SplashScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet("background: #ffffff; border-radius: 24px;")
        self.setFixedSize(600, 400)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(30)

        logo_path = "assets/images/logo_sibibit.png"
        if os.path.exists(logo_path):
            logo_label = QLabel()
            pixmap = QPixmap(logo_path).scaled(180, 180, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            logo_label.setPixmap(pixmap)
            logo_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(logo_label)
        else:
            logo = FishLogo(size=180)
            layout.addWidget(logo, alignment=Qt.AlignCenter)

        subtitle = QLabel("Loading, please wait...")
        subtitle.setStyleSheet("color: #8b5ce6; font-size: 15px;")
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)

        self.progress = QProgressBar()
        self.progress.setObjectName("splashProgress")
        self.progress.setTextVisible(False)
        self.progress.setMaximum(100)
        self.progress.setValue(0)
        self.progress.setFixedHeight(10)
        self.progress.setFixedWidth(400)
        layout.addWidget(self.progress, alignment=Qt.AlignCenter)

        credit = QLabel("Created by    INOTEKAI")
        credit.setStyleSheet("color: #111111; font-size: 12px;")
        credit.setAlignment(Qt.AlignCenter)
        layout.addWidget(credit)

        self._progress_value = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update_progress)
        self.timer.start(30)

    def _update_progress(self):
        self._progress_value += 2
        self.progress.setValue(self._progress_value)
        if self._progress_value >= 100:
            self.timer.stop()
            self.close()
