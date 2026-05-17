from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFrame,
)
from widgets.common import CardFrame


class LoginPage(QWidget):
    login_success = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("loginPage")

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)

        card = CardFrame("loginCard")
        card.setFixedSize(440, 500)
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(44, 44, 44, 44)
        card_layout.setSpacing(24)

        logo = QLabel("S")
        logo.setObjectName("loginLogo")
        logo.setAlignment(Qt.AlignCenter)

        title = QLabel("SiBibit System")
        title.setObjectName("loginTitle")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Silakan login untuk melanjutkan")
        subtitle.setObjectName("loginSubtitle")
        subtitle.setAlignment(Qt.AlignCenter)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setMinimumHeight(50)
        self.username_input.setObjectName("loginInput")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumHeight(50)
        self.password_input.setObjectName("loginInput")
        self.password_input.returnPressed.connect(self._handle_login)

        self.error_label = QLabel("")
        self.error_label.setObjectName("errorLabel")
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.hide()

        login_btn = QPushButton("Login")
        login_btn.setObjectName("loginButton")
        login_btn.setCursor(Qt.PointingHandCursor)
        login_btn.setMinimumHeight(50)
        login_btn.clicked.connect(self._handle_login)

        card_layout.addWidget(logo)
        card_layout.addWidget(title)
        card_layout.addWidget(subtitle)
        card_layout.addSpacing(16)
        card_layout.addWidget(self.username_input)
        card_layout.addWidget(self.password_input)
        card_layout.addWidget(self.error_label)
        card_layout.addWidget(login_btn)
        card_layout.addStretch()

        main_layout.addWidget(card)

    def _handle_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if username and password:
            self.error_label.hide()
            self.login_success.emit()
        else:
            self.error_label.setText("Username dan password tidak boleh kosong")
            self.error_label.show()
