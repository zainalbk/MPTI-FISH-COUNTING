"""
BACKUP ORIGINAL DASHBOARD CODE:
Dashboard dengan dark theme, circular progress, line chart, stat cards.
Disimpan untuk referensi jika perlu rollback.

Original features:
- Live camera placeholder
- Counter card
- 3 stat cards (Sehat, Rusak, Total)
- START/STOP/RESET buttons
- Line chart realtime
- Circular progress
- Data table 5 rows

File: pages/dashboard.py (original dark theme version)
"""

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QScrollArea,
    QPushButton,
)
from widgets.reference_ui import (
    ShadowFrame,
    CameraView,
    MainActionButton,
    SmallMetricCard,
    FishThumbnail,
)
from backend.mock_data import generate_dashboard_metrics


class DashboardPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("dashboardPage")

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.NoFrame)
        scroll.setStyleSheet("QScrollArea { background: #f6f1fb; border: none; }")

        container = QWidget()
        container.setStyleSheet("background: #f6f1fb;")
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(16)

        top_row = QHBoxLayout()
        top_row.setSpacing(16)

        camera_panel = ShadowFrame("panel")
        camera_layout = QVBoxLayout(camera_panel)
        camera_layout.setContentsMargins(8, 8, 8, 8)
        camera_layout.setSpacing(6)
        camera_title = QLabel("📷  Camera Feed")
        camera_title.setObjectName("panelTitle")
        self.camera_view = CameraView(active=False)
        camera_layout.addWidget(camera_title)
        camera_layout.addWidget(self.camera_view)
        top_row.addWidget(camera_panel, 3)

        counter_panel = ShadowFrame("panel")
        counter_layout = QVBoxLayout(counter_panel)
        counter_layout.setContentsMargins(8, 8, 8, 8)
        counter_layout.setSpacing(6)
        counter_title = QLabel("📊  Counter")
        counter_title.setObjectName("panelTitle")
        counter_layout.addWidget(counter_title)
        self.counter_label = QLabel("0")
        self.counter_label.setObjectName("counterBig")
        self.counter_label.setAlignment(Qt.AlignCenter)
        counter_layout.addWidget(self.counter_label)
        counter_unit = QLabel("ekor")
        counter_unit.setObjectName("counterUnit")
        counter_unit.setAlignment(Qt.AlignCenter)
        counter_layout.addWidget(counter_unit)
        counter_layout.addStretch()
        top_row.addWidget(counter_panel, 2)

        main_layout.addLayout(top_row)

        middle_row = QHBoxLayout()
        middle_row.setSpacing(16)

        klasifikasi_panel = ShadowFrame("panel")
        klasifikasi_layout = QVBoxLayout(klasifikasi_panel)
        klasifikasi_layout.setContentsMargins(8, 8, 8, 8)
        klasifikasi_layout.setSpacing(8)

        klas_header = QHBoxLayout()
        klas_title = QLabel("🐟 Klasifikasi Ikan (YoloV8)")
        klas_title.setObjectName("panelTitle")
        klas_header.addWidget(klas_title)
        klas_header.addStretch()
        self.detail_btn = QPushButton("Detail Klasifikasi →")
        self.detail_btn.setObjectName("smallPill")
        self.detail_btn.setCursor(Qt.PointingHandCursor)
        klas_header.addWidget(self.detail_btn)
        klasifikasi_layout.addLayout(klas_header)

        self.table = QTableWidget(4, 3)
        self.table.setObjectName("dataTable")
        self.table.setHorizontalHeaderLabels(["Jenis Ikan", "Jumlah", "Akurasi"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionMode(QTableWidget.NoSelection)
        self.table.setMaximumHeight(180)
        klasifikasi_layout.addWidget(self.table)

        middle_row.addWidget(klasifikasi_panel, 3)

        buttons_grid = QGridLayout()
        buttons_grid.setSpacing(14)
        self.btn_start = MainActionButton("▶  START", "green")
        self.btn_riwayat = MainActionButton("📋  RIWAYAT", "purple")
        self.btn_reset = MainActionButton("↻  RESET", "yellow")
        self.btn_save = MainActionButton("💾  SAVE", "purple")
        buttons_grid.addWidget(self.btn_start, 0, 0)
        buttons_grid.addWidget(self.btn_riwayat, 0, 1)
        buttons_grid.addWidget(self.btn_reset, 1, 0)
        buttons_grid.addWidget(self.btn_save, 1, 1)
        middle_row.addLayout(buttons_grid, 2)

        main_layout.addLayout(middle_row)

        bottom_row = QHBoxLayout()
        bottom_row.setSpacing(14)
        self.metric_total = SmallMetricCard("Total Ekor", "25400")
        self.metric_jenis = SmallMetricCard("Jenis Ikan", "2")
        self.metric_akurasi = SmallMetricCard("Rata-Rata Akurasi", "90.8%")
        bottom_row.addWidget(self.metric_total)
        bottom_row.addWidget(self.metric_jenis)
        bottom_row.addWidget(self.metric_akurasi)
        main_layout.addLayout(bottom_row)
        main_layout.addStretch()

        scroll.setWidget(container)
        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.addWidget(scroll)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update_data)
        self.timer.start(2500)
        self._update_data()

    def _set_metric_value(self, metric_card, value):
        labels = metric_card.findChildren(QLabel)
        if len(labels) >= 2:
            labels[1].setText(value)

    def _update_data(self):
        metrics = generate_dashboard_metrics()
        self.counter_label.setText(f"{metrics['counter']:,}")
        self._set_metric_value(self.metric_total, f"{metrics['total']:,}")
        self._set_metric_value(self.metric_jenis, "4")
        self._set_metric_value(self.metric_akurasi, f"{metrics['accuracy']}%")

        fish_data = [
            ("nila", "Nila", metrics["healthy"], f"{metrics['accuracy']}%"),
            ("lele", "Lele", 302, "97.2%"),
            ("mujair", "Mujair", 12000, "45.2%"),
            ("kapal", "Kapal Laut", 1, "100%"),
        ]

        for row, (fish_type, name, count, acc) in enumerate(fish_data):
            thumb = FishThumbnail(fish_type)
            self.table.setCellWidget(row, 0, thumb)
            item_name = QTableWidgetItem(name)
            self.table.setItem(row, 0, item_name)
            self.table.setItem(row, 1, QTableWidgetItem(str(count)))
            self.table.setItem(row, 2, QTableWidgetItem(acc))
