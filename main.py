"""
BACKUP ORIGINAL MAIN.PY:
Main window dengan dark theme, sidebar menu, login page, 4 halaman utama.
Menggunakan QPalette untuk dark mode.
File: main.py (original version with sidebar navigation)
"""

import sys
from datetime import datetime
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QStackedWidget,
);
from PyQt5.QtGui import QPalette, QColor
from pages.splash import SplashScreen
from pages.dashboard import DashboardPage
from pages.history import HistoryOverviewPage
from pages.history_detail import HistoryDetailPage
from pages.detail_klasifikasi import DetailKlasifikasiPage
from widgets.reference_ui import TopHeader
from widgets.dialogs import SimpanDialog, IntervalWaktuDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SiBibit - Sistem Perhitungan Bibit Ikan")
        self.resize(1280, 800)
        self.setMinimumSize(1024, 600)
        self.setStyleSheet("background: #f6f1fb;")

        root = QWidget()
        root.setStyleSheet("background: #f6f1fb;")
        self.setCentralWidget(root)

        root_layout = QVBoxLayout(root)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        self.header = TopHeader("Sistem Perhitungan Bibit Ikan", show_back=False)
        self.header.power_button.clicked.connect(self.close)
        root_layout.addWidget(self.header)

        self.stack = QStackedWidget()
        self.dashboard_page = DashboardPage()
        self.history_overview_page = HistoryOverviewPage()
        self.history_detail_page = HistoryDetailPage()
        self.detail_klasifikasi_page = DetailKlasifikasiPage()

        self.stack.addWidget(self.dashboard_page)
        self.stack.addWidget(self.history_overview_page)
        self.stack.addWidget(self.history_detail_page)
        self.stack.addWidget(self.detail_klasifikasi_page)

        root_layout.addWidget(self.stack)

        self.dashboard_page.btn_riwayat.clicked.connect(self.show_history_overview)
        self.dashboard_page.detail_btn.clicked.connect(self.show_detail_klasifikasi)
        self.dashboard_page.btn_save.clicked.connect(self.show_simpan_dialog)
        self.dashboard_page.btn_reset.clicked.connect(self.show_interval_dialog)
        self.history_overview_page.detail_btn.clicked.connect(self.show_history_detail)
        
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self._update_clock)
        self.clock_timer.start(1000)
        self._update_clock()

        self.show_dashboard()

    def _update_clock(self):
        date_text = datetime.now().strftime("📅  %d %b %Y, %I:%M %p WIB")
        if hasattr(self.header, 'findChild'):
            from PyQt5.QtWidgets import QLabel
            date_label = self.header.findChild(QLabel, "dateBadge")
            if date_label:
                date_label.setText(date_text)

    def show_dashboard(self):
        self.stack.setCurrentWidget(self.dashboard_page)
        self.header.setParent(None)
        self.header = TopHeader("Sistem Perhitungan Bibit Ikan", show_back=False)
        self.header.power_button.clicked.connect(self.close)
        self.centralWidget().layout().insertWidget(0, self.header)

    def show_history_overview(self):
        self.stack.setCurrentWidget(self.history_overview_page)
        self.header.setParent(None)
        self.header = TopHeader("Riwayat", show_back=True)
        self.header.back_button.clicked.connect(self.show_dashboard)
        self.header.power_button.clicked.connect(self.close)
        self.centralWidget().layout().insertWidget(0, self.header)

    def show_history_detail(self):
        self.stack.setCurrentWidget(self.history_detail_page)
        self.header.setParent(None)
        self.header = TopHeader("Riwayat", show_back=True)
        self.header.back_button.clicked.connect(self.show_history_overview)
        self.header.power_button.clicked.connect(self.close)
        self.centralWidget().layout().insertWidget(0, self.header)

    def show_simpan_dialog(self):
        dialog = SimpanDialog(self)
        dialog.exec_()

    def show_interval_dialog(self):
        dialog = IntervalWaktuDialog(self)
        dialog.exec_()

    def show_detail_klasifikasi(self):
        self.stack.setCurrentWidget(self.detail_klasifikasi_page)
        self.header.setParent(None)
        self.header = TopHeader("Detail Klasifikasi", show_back=True)
        self.header.back_button.clicked.connect(self.show_dashboard)
        self.header.power_button.clicked.connect(self.close)
        self.centralWidget().layout().insertWidget(0, self.header)


def load_stylesheet(app):
    try:
        with open("styles/theme.qss", "r", encoding="utf-8") as file:
            qss = file.read()
            app.setStyleSheet(qss)
            print("Stylesheet loaded successfully")
    except Exception as e:
        print(f"Warning: Could not load stylesheet - {e}")


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    app.setApplicationName("SiBibit")
    app.setStyle("Fusion")
    
    load_stylesheet(app)

    splash = SplashScreen()
    splash.show()

    window = MainWindow()

    def show_main_window():
        window.show()
        app.setQuitOnLastWindowClosed(True)

    QTimer.singleShot(3200, show_main_window)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

