from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from widgets.common import CardFrame


class Sidebar(QWidget):
    menu_clicked = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("sidebar")
        self.setFixedWidth(240)
        self._collapsed = False
        self._active_menu = "Dashboard"

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        logo_frame = QFrame()
        logo_frame.setObjectName("logoFrame")
        logo_frame.setFixedHeight(80)
        logo_layout = QVBoxLayout(logo_frame)
        logo_layout.setAlignment(Qt.AlignCenter)
        self.logo_label = QLabel("S")
        self.logo_label.setObjectName("logoText")
        self.logo_label.setAlignment(Qt.AlignCenter)
        logo_layout.addWidget(self.logo_label)
        layout.addWidget(logo_frame)

        menu_frame = QFrame()
        menu_frame.setObjectName("menuFrame")
        menu_layout = QVBoxLayout(menu_frame)
        menu_layout.setContentsMargins(12, 20, 12, 20)
        menu_layout.setSpacing(8)

        self.menu_buttons = {}
        menus = ["Dashboard", "Riwayat", "Statistik", "Pengaturan"]
        for menu in menus:
            btn = QPushButton(menu)
            btn.setObjectName("menuButton")
            btn.setProperty("fullText", menu)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setMinimumHeight(48)
            btn.clicked.connect(lambda checked, m=menu: self._on_menu_click(m))
            menu_layout.addWidget(btn)
            self.menu_buttons[menu] = btn

        menu_layout.addStretch()

        logout_btn = QPushButton("Logout")
        logout_btn.setObjectName("logoutButton")
        logout_btn.setCursor(Qt.PointingHandCursor)
        logout_btn.setMinimumHeight(48)
        logout_btn.clicked.connect(lambda: self.menu_clicked.emit("Logout"))
        menu_layout.addWidget(logout_btn)

        layout.addWidget(menu_frame)

        self._update_active_style()

    def _on_menu_click(self, menu_name):
        self._active_menu = menu_name
        self._update_active_style()
        self.menu_clicked.emit(menu_name)

    def _update_active_style(self):
        for name, btn in self.menu_buttons.items():
            if name == self._active_menu:
                btn.setProperty("active", True)
            else:
                btn.setProperty("active", False)
            btn.style().unpolish(btn)
            btn.style().polish(btn)
