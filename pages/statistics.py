from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QScrollArea,
    QComboBox,
)
from widgets.common import CardFrame, SectionTitle, StatCard
from widgets.charts import BarChart, LineChart, PieChart
from backend.mock_data import generate_statistical_data


class StatisticsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("statisticsPage")

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.NoFrame)

        container = QWidget()
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(28, 28, 28, 28)
        main_layout.setSpacing(24)

        header = QHBoxLayout()
        title = SectionTitle("Statistik & Analisis")
        header.addWidget(title)
        header.addStretch()

        period_combo = QComboBox()
        period_combo.addItems(["Harian", "Mingguan", "Bulanan"])
        period_combo.setMinimumHeight(44)
        period_combo.setMinimumWidth(160)
        header.addWidget(period_combo)
        main_layout.addLayout(header)

        summary_grid = QGridLayout()
        summary_grid.setSpacing(18)
        stat1 = StatCard("Rata-rata Harian", "1,245", "#9d7bff")
        stat2 = StatCard("Akurasi Rata-rata", "94.8%", "#ffa726")
        stat3 = StatCard("Total Minggu Ini", "8,715", "#ff6b9d")
        stat4 = StatCard("Efisiensi Sistem", "92%", "#4caf50")
        summary_grid.addWidget(stat1, 0, 0)
        summary_grid.addWidget(stat2, 0, 1)
        summary_grid.addWidget(stat3, 0, 2)
        summary_grid.addWidget(stat4, 0, 3)
        main_layout.addLayout(summary_grid)

        bar_card = CardFrame()
        bar_layout = QVBoxLayout(bar_card)
        bar_layout.setContentsMargins(24, 24, 24, 24)
        bar_layout.setSpacing(16)
        bar_title = SectionTitle("Produksi Mingguan")
        self.bar_chart = BarChart()
        bar_layout.addWidget(bar_title)
        bar_layout.addWidget(self.bar_chart)
        main_layout.addWidget(bar_card)

        charts_row = QHBoxLayout()
        charts_row.setSpacing(20)

        line_card = CardFrame()
        line_layout = QVBoxLayout(line_card)
        line_layout.setContentsMargins(24, 24, 24, 24)
        line_layout.setSpacing(16)
        line_title = SectionTitle("Tren Bulanan")
        self.line_chart = LineChart()
        line_layout.addWidget(line_title)
        line_layout.addWidget(self.line_chart)
        charts_row.addWidget(line_card, 2)

        pie_card = CardFrame()
        pie_layout = QVBoxLayout(pie_card)
        pie_layout.setContentsMargins(24, 24, 24, 24)
        pie_layout.setSpacing(16)
        pie_title = SectionTitle("Distribusi Status")
        self.pie_chart = PieChart()
        pie_layout.addWidget(pie_title)
        pie_layout.addWidget(self.pie_chart, alignment=Qt.AlignCenter)
        charts_row.addWidget(pie_card, 1)

        main_layout.addLayout(charts_row)

        scroll.setWidget(container)
        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.addWidget(scroll)

        self._load_data()

    def _load_data(self):
        data = generate_statistical_data()
        self.bar_chart.set_data(data["bar_labels"], data["bar_values"])
        self.line_chart.set_data(data["line_values"])
        self.pie_chart.set_data(data["pie_values"])
