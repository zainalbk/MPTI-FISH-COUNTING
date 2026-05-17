"""
Detail Klasifikasi Page - Menampilkan breakdown per jenis ikan, pie chart, video preview
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
    QFrame,
)
from PyQt5.QtGui import QPainter, QColor
from widgets.reference_ui import ShadowFrame


class PieChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(220, 220)
        self.data = [
            ("Nila", 285, "#8b5ce6"),
            ("Lele", 302, "#5ec8e6"),
            ("Mujair", 12000, "#4caf50"),
            ("Kapal Laut", 1, "#f86b7a"),
        ]

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        total = sum(count for _, count, _ in self.data)
        if total == 0:
            return
        
        rect = self.rect().adjusted(10, 10, -10, -10)
        start_angle = 0
        
        for name, count, color in self.data:
            span = int((count / total) * 360 * 16)
            painter.setBrush(QColor(color))
            painter.setPen(Qt.NoPen)
            painter.drawPie(rect, start_angle, span)
            start_angle += span


class VideoPreview(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background: #233142; border-radius: 12px;")
        self.setMinimumHeight(180)
        
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        
        play_btn = QLabel("▶")
        play_btn.setStyleSheet("color: #ffffff; font-size: 48px; background: transparent;")
        play_btn.setAlignment(Qt.AlignCenter)
        layout.addWidget(play_btn)
        
        progress = QFrame()
        progress.setStyleSheet("background: #8b5ce6; border-radius: 2px;")
        progress.setFixedHeight(4)
        progress.setFixedWidth(200)
        layout.addWidget(progress, alignment=Qt.AlignCenter)


class DetailKlasifikasiPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("detailKlasifikasiPage")

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.NoFrame)
        scroll.setStyleSheet("QScrollArea { background: #f6f1fb; border: none; }")

        container = QWidget()
        container.setStyleSheet("background: #f6f1fb;")
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(16)

        content_row = QHBoxLayout()
        content_row.setSpacing(16)

        left_panel = ShadowFrame("whiteCard")
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(20, 20, 20, 20)
        left_layout.setSpacing(16)

        title = QLabel("Detail Hasil Perhitungan")
        title.setStyleSheet("background: transparent; color: #111111; font-size: 16px; font-weight: bold;")
        left_layout.addWidget(title)

        self.table = QTableWidget(4, 4)
        self.table.setHorizontalHeaderLabels(["No.", "Jenis Ikan", "Jumlah (ekor)", "Persentase (%)"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionMode(QTableWidget.NoSelection)
        self.table.setMaximumHeight(200)
        
        fish_data = [
            ("1", "● Nila", "285", "71.2%"),
            ("2", "● Lele", "302", "25.6%"),
            ("3", "● Mujair", "12000", "3.2%"),
            ("4", "● Kapal Laut", "1", "3.2%"),
        ]
        for row, data in enumerate(fish_data):
            for col, val in enumerate(data):
                item = QTableWidgetItem(val)
                if col == 1:
                    if "Nila" in val:
                        item.setForeground(QColor("#8b5ce6"))
                    elif "Lele" in val:
                        item.setForeground(QColor("#5ec8e6"))
                    elif "Mujair" in val:
                        item.setForeground(QColor("#4caf50"))
                    else:
                        item.setForeground(QColor("#f86b7a"))
                self.table.setItem(row, col, item)
        
        left_layout.addWidget(self.table)

        total_row = QHBoxLayout()
        total_label = QLabel("Total")
        total_label.setStyleSheet("color: #7b61ff; font-size: 14px; font-weight: bold;")
        total_value = QLabel("12588")
        total_value.setStyleSheet("color: #7b61ff; font-size: 14px; font-weight: bold;")
        total_pct = QLabel("100%")
        total_pct.setStyleSheet("color: #7b61ff; font-size: 14px; font-weight: bold;")
        total_row.addWidget(total_label)
        total_row.addStretch()
        total_row.addWidget(total_value)
        total_row.addWidget(total_pct)
        left_layout.addLayout(total_row)

        meta_row = QHBoxLayout()
        date_badge = QLabel("📅 22 May 2026, 07:00 AM WIB")
        date_badge.setStyleSheet("background: #e6d5ff; color: #111111; border-radius: 8px; padding: 6px 12px; font-size: 11px;")
        kolam_badge = QLabel("Kolam:     1  ▼")
        kolam_badge.setStyleSheet("background: #e6d5ff; color: #111111; border-radius: 8px; padding: 6px 12px; font-size: 11px;")
        meta_row.addWidget(date_badge)
        meta_row.addWidget(kolam_badge)
        meta_row.addStretch()
        left_layout.addLayout(meta_row)

        left_layout.addStretch()
        content_row.addWidget(left_panel, 1)

        right_col = QVBoxLayout()
        right_col.setSpacing(16)

        video_panel = ShadowFrame("whiteCard")
        video_layout = QVBoxLayout(video_panel)
        video_layout.setContentsMargins(16, 16, 16, 16)
        video_layout.setSpacing(10)
        video_title = QLabel("Preview Hasil Klasifikasi")
        video_title.setStyleSheet("background: transparent; color: #111111; font-size: 14px; font-weight: bold;")
        video_layout.addWidget(video_title)
        video_preview = VideoPreview()
        video_layout.addWidget(video_preview)
        right_col.addWidget(video_panel)

        pie_panel = ShadowFrame("whiteCard")
        pie_layout = QVBoxLayout(pie_panel)
        pie_layout.setContentsMargins(16, 16, 16, 16)
        pie_layout.setSpacing(10)
        pie_title = QLabel("Ringkasan Perhitungan")
        pie_title.setStyleSheet("background: transparent; color: #111111; font-size: 14px; font-weight: bold;")
        pie_layout.addWidget(pie_title)
        
        pie_chart = PieChartWidget()
        pie_layout.addWidget(pie_chart, alignment=Qt.AlignCenter)
        
        legend_layout = QVBoxLayout()
        legend_layout.setSpacing(6)
        for name, count, color in pie_chart.data:
            leg = QHBoxLayout()
            dot = QLabel("●")
            dot.setStyleSheet(f"color: {color}; font-size: 16px;")
            leg.addWidget(dot)
            leg.addWidget(QLabel(name))
            leg.addStretch()
            leg.addWidget(QLabel(str(count)))
            legend_layout.addLayout(leg)
        pie_layout.addLayout(legend_layout)
        
        summary_row = QHBoxLayout()
        summary_row.setSpacing(10)
        total_card = ShadowFrame("softCard")
        total_card_layout = QVBoxLayout(total_card)
        total_card_layout.setContentsMargins(8, 8, 8, 8)
        total_card_layout.addWidget(QLabel("Total Ikan Terdeteksi"))
        total_val = QLabel("1 250 ekor")
        total_val.setStyleSheet("color: #7b61ff; font-size: 16px; font-weight: bold;")
        total_card_layout.addWidget(total_val)
        
        acc_card = ShadowFrame("softCard")
        acc_card_layout = QVBoxLayout(acc_card)
        acc_card_layout.setContentsMargins(8, 8, 8, 8)
        acc_card_layout.addWidget(QLabel("Rata-Rata Akurasi"))
        acc_val = QLabel("97.6%")
        acc_val.setStyleSheet("color: #7b61ff; font-size: 16px; font-weight: bold;")
        acc_card_layout.addWidget(acc_val)
        
        summary_row.addWidget(total_card)
        summary_row.addWidget(acc_card)
        pie_layout.addLayout(summary_row)
        
        action_row = QHBoxLayout()
        action_row.setSpacing(10)
        delete_btn = QPushButton("🗑  DELETE")
        delete_btn.setObjectName("deleteButton")
        delete_btn.setMinimumHeight(44)
        save_btn = QPushButton("💾  SAVE")
        save_btn.setObjectName("saveButton")
        save_btn.setMinimumHeight(44)
        action_row.addWidget(delete_btn)
        action_row.addWidget(save_btn)
        pie_layout.addLayout(action_row)
        
        right_col.addWidget(pie_panel)
        content_row.addLayout(right_col, 1)

        main_layout.addLayout(content_row)
        main_layout.addStretch()

        scroll.setWidget(container)
        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.addWidget(scroll)
