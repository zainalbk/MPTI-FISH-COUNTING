from PyQt5.QtCore import Qt, QRectF, QSize
from PyQt5.QtGui import QColor, QPainter, QPen, QFont
from PyQt5.QtWidgets import (
    QWidget,
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGraphicsDropShadowEffect,
    QLineEdit,
)


class CardFrame(QFrame):
    def __init__(self, class_name="card", parent=None):
        super().__init__(parent)
        self.setObjectName(class_name)
        self.setFrameShape(QFrame.StyledPanel)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(32)
        shadow.setXOffset(0)
        shadow.setYOffset(10)
        shadow.setColor(QColor(0, 0, 0, 100))
        self.setGraphicsEffect(shadow)


class SectionTitle(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setObjectName("sectionTitle")


class PrimaryButton(QPushButton):
    def __init__(self, text, variant="primary", parent=None):
        super().__init__(text, parent)
        self.setProperty("variant", variant)
        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumHeight(46)


class SearchInput(QLineEdit):
    def __init__(self, placeholder="Cari data...", parent=None):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setMinimumHeight(44)


class CircularProgress(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._value = 72
        self._label = "Kinerja"
        self.setMinimumSize(200, 200)

    def set_value(self, value):
        self._value = max(0, min(100, value))
        self.update()

    def set_label(self, text):
        self._label = text
        self.update()

    def sizeHint(self):
        return QSize(200, 200)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = QRectF(20, 20, self.width() - 40, self.height() - 40)

        bg_pen = QPen(QColor("#2c2440"), 16)
        bg_pen.setCapStyle(Qt.RoundCap)
        painter.setPen(bg_pen)
        painter.drawArc(rect, 0, 360 * 16)

        fg_pen = QPen(QColor("#9d7bff"), 16)
        fg_pen.setCapStyle(Qt.RoundCap)
        painter.setPen(fg_pen)
        start_angle = 90 * 16
        span = int(-self._value / 100 * 360 * 16)
        painter.drawArc(rect, start_angle, span)

        painter.setPen(QColor("#ffffff"))
        font = QFont("Segoe UI", 28, QFont.Bold)
        painter.setFont(font)
        painter.drawText(self.rect(), Qt.AlignCenter, f"{self._value}%")

        painter.setPen(QColor("#9d8bb8"))
        font2 = QFont("Segoe UI", 11)
        painter.setFont(font2)
        painter.drawText(self.rect().adjusted(0, 65, 0, 0), Qt.AlignCenter, self._label)


class StatCard(CardFrame):
    def __init__(self, title, value="0", accent="#9d7bff", parent=None):
        super().__init__(parent=parent)
        self.setObjectName("statCard")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(22, 22, 22, 22)
        layout.setSpacing(10)

        self.title_label = QLabel(title)
        self.title_label.setObjectName("cardTitle")
        self.value_label = QLabel(str(value))
        self.value_label.setObjectName("cardValue")
        self.value_label.setStyleSheet(f"color: {accent};")

        layout.addWidget(self.title_label)
        layout.addWidget(self.value_label)

    def set_value(self, value):
        self.value_label.setText(str(value))


def make_placeholder_camera(title="Live Camera"):
    card = CardFrame()
    layout = QVBoxLayout(card)
    layout.setContentsMargins(20, 20, 20, 20)
    layout.setSpacing(14)

    title_label = QLabel(title)
    title_label.setObjectName("cardTitle")
    preview = QLabel("📷\n\nCAMERA PLACEHOLDER\nDummy Stream Active")
    preview.setAlignment(Qt.AlignCenter)
    preview.setObjectName("cameraPlaceholder")
    preview.setMinimumHeight(260)

    layout.addWidget(title_label)
    layout.addWidget(preview)
    return card
