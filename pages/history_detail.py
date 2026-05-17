"""
History Detail Page - Tabel riwayat dengan nama, tanggal, jam, total ikan, akurasi
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QScrollArea,
    QPushButton,
)
from widgets.reference_ui import ShadowFrame, SmallMetricCard
from backend.mock_data import generate_history_rows


class HistoryDetailPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("historyDetailPage")

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.NoFrame)
        scroll.setStyleSheet("QScrollArea { background: #f6f1fb; border: none; }")

        container = QWidget()
        container.setStyleSheet("background: #f6f1fb;")
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(16)

        top_bar = QHBoxLayout()
        date_range = QLabel("▼ 13 April - 19 April 2026")
        date_range.setStyleSheet("background: #e6d5ff; color: #111111; border-radius: 8px; padding: 8px 16px; font-size: 13px;")
        top_bar.addWidget(date_range)
        top_bar.addStretch()
        main_layout.addLayout(top_bar)

        metrics_row = QHBoxLayout()
        metrics_row.setSpacing(14)
        self.metric_total = SmallMetricCard("Total Ekor", "25400")
        self.metric_jenis = SmallMetricCard("Jenis Ikan", "2")
        self.metric_akurasi = SmallMetricCard("Rata-Rata Akurasi", "90.8%")
        kolam_card = ShadowFrame("softCard")
        kolam_layout = QVBoxLayout(kolam_card)
        kolam_layout.setContentsMargins(12, 10, 12, 10)
        kolam_label = QLabel("Kolam :")
        kolam_label.setStyleSheet("background: transparent; color: #111111; font-size: 16px;")
        kolam_value = QLabel("1  ▼")
        kolam_value.setStyleSheet("background: transparent; color: #7b61ff; font-size: 26px; font-weight: bold;")
        kolam_layout.addWidget(kolam_label)
        kolam_layout.addWidget(kolam_value)
        metrics_row.addWidget(self.metric_total)
        metrics_row.addWidget(self.metric_jenis)
        metrics_row.addWidget(self.metric_akurasi)
        metrics_row.addWidget(kolam_card)
        main_layout.addLayout(metrics_row)

        table_panel = ShadowFrame("whiteCard")
        table_layout = QVBoxLayout(table_panel)
        table_layout.setContentsMargins(20, 20, 20, 20)
        table_layout.setSpacing(12)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Nama", "Tanggal", "Jam", "Total Ikan", "Rata-Rata Akurasi"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setMinimumHeight(400)
        table_layout.addWidget(self.table)

        main_layout.addWidget(table_panel)
        main_layout.addStretch()

        scroll.setWidget(container)
        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.addWidget(scroll)

        self._load_data()

    def _load_data(self):
        rows = generate_history_rows(10)
        self.table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            name_item = QTableWidgetItem("Budiono Siregar")
            date_item = QTableWidgetItem("22/4/2026")
            time_item = QTableWidgetItem("07:00 AM WIB")
            total_item = QTableWidgetItem("1250")
            acc_item = QTableWidgetItem("94%")
            
            arrow_item = QTableWidgetItem("→")
            arrow_item.setForeground(Qt.blue)
            
            self.table.setItem(i, 0, name_item)
            self.table.setItem(i, 1, date_item)
            self.table.setItem(i, 2, time_item)
            self.table.setItem(i, 3, total_item)
            self.table.setItem(i, 4, acc_item)
