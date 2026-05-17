"""
BACKUP ORIGINAL HISTORY CODE:
History page dengan dark theme, search bar, filter combo, export button, 
pagination, dan tabel 40 rows.

Original features:
- Search input
- Filter combo (Semua Status, Sehat, Rusak, Perlu Cek)
- Export CSV button
- Large table with 6 columns
- Pagination controls

File: pages/history.py (original dark theme version)
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QScrollArea,
)
from PyQt5.QtGui import QColor, QPainter, QFont
from widgets.reference_ui import TopHeader, ShadowFrame, SmallMetricCard
from widgets.charts import BarChart
from backend.mock_data import generate_statistical_data


class HistoryOverviewPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("historyPage")

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
        top_bar.setSpacing(12)

        period_label = QLabel("Periode")
        period_label.setStyleSheet("color: #111111; font-size: 14px;")
        top_bar.addWidget(period_label)

        self.period_combo = QComboBox()
        self.period_combo.addItems(["Mingguan", "Harian", "Bulanan"])
        self.period_combo.setFixedHeight(36)
        self.period_combo.setStyleSheet("background: #ffffff; border: 1px solid #111111; border-radius: 6px; padding: 4px 10px;")
        top_bar.addWidget(self.period_combo)

        date_range = QLabel("13 April - 19 April 2026")
        date_range.setStyleSheet("background: #e6d5ff; color: #111111; border-radius: 8px; padding: 8px 16px; font-size: 13px;")
        top_bar.addWidget(date_range)

        top_bar.addStretch()

        self.detail_btn = QPushButton("Detail Riwayat →")
        self.detail_btn.setObjectName("smallPill")
        self.detail_btn.setCursor(Qt.PointingHandCursor)
        top_bar.addWidget(self.detail_btn)

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

        chart_panel = ShadowFrame("whiteCard")
        chart_layout = QVBoxLayout(chart_panel)
        chart_layout.setContentsMargins(20, 20, 20, 20)
        chart_layout.setSpacing(12)
        chart_title = QLabel("Riwayat Counting")
        chart_title.setStyleSheet("background: transparent; color: #111111; font-size: 16px; font-weight: bold;")
        chart_layout.addWidget(chart_title)

        self.bar_chart = BarChart()
        self.bar_chart.setMinimumHeight(280)
        chart_layout.addWidget(self.bar_chart)

        legend = QHBoxLayout()
        legend.setSpacing(20)
        nila_legend = QLabel("■ Nila")
        nila_legend.setStyleSheet("color: #8b5ce6; font-size: 12px;")
        lele_legend = QLabel("■ Lele")
        lele_legend.setStyleSheet("color: #5ec8e6; font-size: 12px;")
        legend.addStretch()
        legend.addWidget(nila_legend)
        legend.addWidget(lele_legend)
        legend.addStretch()
        chart_layout.addLayout(legend)

        main_layout.addWidget(chart_panel)
        main_layout.addStretch()

        scroll.setWidget(container)
        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.addWidget(scroll)

        self._load_data()

    def _load_data(self):
        data = generate_statistical_data()
        self.bar_chart.set_data(data["bar_labels"], data["bar_values"])

