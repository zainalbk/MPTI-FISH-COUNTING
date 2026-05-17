from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QScrollArea,
    QLabel,
    QLineEdit,
    QCheckBox,
    QSlider,
    QSpinBox,
)
from widgets.common import CardFrame, SectionTitle, PrimaryButton


class SettingsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("settingsPage")

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.NoFrame)

        container = QWidget()
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(28, 28, 28, 28)
        main_layout.setSpacing(24)

        title = SectionTitle("Pengaturan Sistem")
        main_layout.addWidget(title)

        general_card = CardFrame()
        general_layout = QVBoxLayout(general_card)
        general_layout.setContentsMargins(24, 24, 24, 24)
        general_layout.setSpacing(20)
        general_title = QLabel("Umum")
        general_title.setObjectName("cardTitle")
        general_layout.addWidget(general_title)

        grid = QGridLayout()
        grid.setSpacing(18)
        grid.setColumnStretch(1, 1)

        grid.addWidget(QLabel("Nama Sistem:"), 0, 0)
        self.system_name = QLineEdit("SiBibit Dashboard")
        self.system_name.setMinimumHeight(44)
        grid.addWidget(self.system_name, 0, 1)

        grid.addWidget(QLabel("Interval Update (detik):"), 1, 0)
        self.interval_spin = QSpinBox()
        self.interval_spin.setRange(1, 60)
        self.interval_spin.setValue(5)
        self.interval_spin.setMinimumHeight(44)
        grid.addWidget(self.interval_spin, 1, 1)

        grid.addWidget(QLabel("Notifikasi:"), 2, 0)
        self.notif_check = QCheckBox("Aktifkan notifikasi")
        self.notif_check.setChecked(True)
        grid.addWidget(self.notif_check, 2, 1)

        general_layout.addLayout(grid)
        main_layout.addWidget(general_card)

        display_card = CardFrame()
        display_layout = QVBoxLayout(display_card)
        display_layout.setContentsMargins(24, 24, 24, 24)
        display_layout.setSpacing(20)
        display_title = QLabel("Tampilan")
        display_title.setObjectName("cardTitle")
        display_layout.addWidget(display_title)

        theme_row = QHBoxLayout()
        theme_row.setSpacing(16)
        theme_row.addWidget(QLabel("Tema:"))
        self.theme_dark = QCheckBox("Dark Mode")
        self.theme_dark.setChecked(True)
        theme_row.addWidget(self.theme_dark)
        self.theme_light = QCheckBox("Light Mode")
        theme_row.addWidget(self.theme_light)
        theme_row.addStretch()
        display_layout.addLayout(theme_row)

        brightness_row = QHBoxLayout()
        brightness_row.setSpacing(16)
        brightness_row.addWidget(QLabel("Kecerahan UI:"))
        self.brightness_slider = QSlider(Qt.Horizontal)
        self.brightness_slider.setRange(50, 100)
        self.brightness_slider.setValue(85)
        brightness_row.addWidget(self.brightness_slider, 1)
        self.brightness_label = QLabel("85%")
        self.brightness_label.setMinimumWidth(50)
        brightness_row.addWidget(self.brightness_label)
        self.brightness_slider.valueChanged.connect(
            lambda v: self.brightness_label.setText(f"{v}%")
        )
        display_layout.addLayout(brightness_row)

        main_layout.addWidget(display_card)

        action_card = CardFrame()
        action_layout = QVBoxLayout(action_card)
        action_layout.setContentsMargins(24, 24, 24, 24)
        action_layout.setSpacing(20)
        action_title = QLabel("Aksi Sistem")
        action_title.setObjectName("cardTitle")
        action_layout.addWidget(action_title)

        btn_row = QHBoxLayout()
        btn_row.setSpacing(14)
        save_btn = PrimaryButton("Simpan Pengaturan", "primary")
        reset_btn = PrimaryButton("Reset ke Default", "secondary")
        calibrate_btn = PrimaryButton("Kalibrasi Sensor", "warning")
        save_btn.setMinimumWidth(160)
        reset_btn.setMinimumWidth(160)
        calibrate_btn.setMinimumWidth(160)
        btn_row.addWidget(save_btn)
        btn_row.addWidget(reset_btn)
        btn_row.addWidget(calibrate_btn)
        btn_row.addStretch()
        action_layout.addLayout(btn_row)
        main_layout.addWidget(action_card)

        main_layout.addStretch()

        scroll.setWidget(container)
        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.addWidget(scroll)
