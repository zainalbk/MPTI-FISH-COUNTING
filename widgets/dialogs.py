"""
Popup Dialogs - Simpan dan Interval Waktu
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QCheckBox,
)
from widgets.reference_ui import ShadowFrame


class SimpanDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Simpan")
        self.setModal(True)
        self.setFixedSize(340, 280)
        self.setStyleSheet("background: #f0ecff; border-radius: 16px;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        title = QLabel("Simpan")
        title.setStyleSheet("color: #111111; font-size: 18px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        input_label = QLabel("Simpan Sebagai....")
        input_label.setStyleSheet("color: #111111; font-size: 13px;")
        layout.addWidget(input_label)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nama file")
        self.name_input.setStyleSheet("""
            background: #ffffff;
            border: 1px solid #cccccc;
            border-radius: 8px;
            padding: 10px;
            font-size: 13px;
        """)
        layout.addWidget(self.name_input)

        kolam_label = QLabel("Kolam")
        kolam_label.setStyleSheet("color: #111111; font-size: 13px;")
        layout.addWidget(kolam_label)

        self.kolam_combo = QComboBox()
        self.kolam_combo.addItems(["1", "2", "3", "4", "5"])
        self.kolam_combo.setStyleSheet("""
            background: #ffffff;
            border: 1px solid #cccccc;
            border-radius: 8px;
            padding: 8px;
            font-size: 13px;
        """)
        layout.addWidget(self.kolam_combo)

        layout.addStretch()

        btn_row = QHBoxLayout()
        btn_row.setSpacing(12)

        confirm_btn = QPushButton("✓  CONFIRM")
        confirm_btn.setStyleSheet("""
            background: #b9f6bf;
            color: #111111;
            border: 1px solid #111111;
            border-radius: 12px;
            padding: 12px;
            font-size: 14px;
            font-weight: bold;
        """)
        confirm_btn.clicked.connect(self.accept)

        cancel_btn = QPushButton("←  BATAL")
        cancel_btn.setStyleSheet("""
            background: #f86b7a;
            color: #111111;
            border: 1px solid #111111;
            border-radius: 12px;
            padding: 12px;
            font-size: 14px;
            font-weight: bold;
        """)
        cancel_btn.clicked.connect(self.reject)

        btn_row.addWidget(confirm_btn)
        btn_row.addWidget(cancel_btn)
        layout.addLayout(btn_row)


class IntervalWaktuDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Interval Waktu")
        self.setModal(True)
        self.setFixedSize(340, 320)
        self.setStyleSheet("background: #f0ecff; border-radius: 16px;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(20)

        title = QLabel("Interval Waktu")
        title.setStyleSheet("color: #111111; font-size: 18px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        grid = QVBoxLayout()
        grid.setSpacing(16)

        options = [
            ("📅\nPilih tanggal", "date"),
            ("📅\nTahunan", "year"),
            ("📅\nMingguan", "week"),
            ("📅\nBulan", "month"),
        ]

        for i in range(0, len(options), 2):
            row = QHBoxLayout()
            row.setSpacing(12)
            for j in range(2):
                if i + j < len(options):
                    text, key = options[i + j]
                    btn = QPushButton(text)
                    btn.setStyleSheet("""
                        background: #ffffff;
                        border: 1px solid #cccccc;
                        border-radius: 12px;
                        padding: 20px;
                        font-size: 12px;
                        text-align: center;
                    """)
                    btn.setMinimumHeight(80)
                    row.addWidget(btn)
            grid.addLayout(row)

        layout.addLayout(grid)
        layout.addStretch()

        cancel_btn = QPushButton("Batal")
        cancel_btn.setStyleSheet("""
            background: #f86b7a;
            color: #111111;
            border: 1px solid #111111;
            border-radius: 8px;
            padding: 10px;
            font-size: 13px;
        """)
        cancel_btn.clicked.connect(self.reject)
        layout.addWidget(cancel_btn, alignment=Qt.AlignRight)
