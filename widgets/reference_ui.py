from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QColor, QPainter, QPen, QBrush, QFont, QPixmap
from PyQt5.QtWidgets import QFrame, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGraphicsDropShadowEffect
import os


class ShadowFrame(QFrame):
    def __init__(self, object_name="whiteCard", parent=None):
        super().__init__(parent)
        self.setObjectName(object_name)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setXOffset(0)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 55))
        self.setGraphicsEffect(shadow)


class TopHeader(QFrame):
    def __init__(self, title="Sistem Perhitungan Bibit Ikan", show_back=False, parent=None):
        super().__init__(parent)
        self.setObjectName("topHeader")
        self.setFixedHeight(64)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 0, 18, 0)
        layout.setSpacing(10)

        logo_path = "assets/images/logo_sibibit.png"
        if os.path.exists(logo_path):
            logo = QLabel()
            pixmap = QPixmap(logo_path).scaled(36, 36, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            logo.setPixmap(pixmap)
        else:
            logo = QLabel("🐟")
            logo.setStyleSheet("font-size: 24px;")
        logo.setFixedSize(36, 36)
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo)

        if show_back:
            back = QPushButton("←")
            back.setObjectName("backButton")
            back.setFixedSize(34, 28)
            layout.addWidget(back)
            self.back_button = back
        else:
            self.back_button = None

        title_label = QLabel(title)
        title_label.setObjectName("headerTitle")
        layout.addWidget(title_label)
        layout.addStretch()

        date = QLabel("📅  27 May 2026, 10:00 AM WIB")
        date.setObjectName("dateBadge")
        date.setAlignment(Qt.AlignCenter)
        date.setFixedHeight(32)
        layout.addWidget(date)

        power = QPushButton("⏻")
        power.setObjectName("powerButton")
        power.setFixedSize(62, 56)
        layout.addWidget(power)
        self.power_button = power


class FishLogo(QLabel):
    def __init__(self, size=170, parent=None):
        super().__init__(parent)
        self.setFixedSize(size, size)
        self.size_value = size
        
        logo_path = "assets/images/logo_sibibit.png"
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path).scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(pixmap)
            self.setAlignment(Qt.AlignCenter)
        else:
            pass

    def paintEvent(self, event):
        if self.pixmap() and not self.pixmap().isNull():
            super().paintEvent(event)
            return
            
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(QColor("#741dff"), 5)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        s = self.size_value
        painter.drawEllipse(25, 35, s - 55, s - 70)
        painter.drawLine(s - 40, s // 2, s - 8, s // 2 - 25)
        painter.drawLine(s - 40, s // 2, s - 8, s // 2 + 25)
        painter.drawLine(s - 8, s // 2 - 25, s - 8, s // 2 + 25)
        painter.setBrush(QColor("#741dff"))
        painter.drawEllipse(s - 55, s // 2 - 20, 8, 8)
        painter.setFont(QFont("Segoe UI", max(18, s // 6), QFont.Bold))
        painter.drawText(self.rect(), Qt.AlignCenter, "sibibit")


class CameraView(QFrame):
    def __init__(self, active=False, parent=None):
        super().__init__(parent)
        self.active = active
        self.setObjectName("cameraPlaceholder")
        self.setMinimumHeight(230)

    def set_active(self, active):
        self.active = active
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect()
        painter.fillRect(rect, QColor("#d9d9d9"))
        if self.active:
            painter.fillRect(rect, QColor("#233142"))
            painter.setPen(QPen(QColor("#8a8f94"), 2))
            for x in range(-100, self.width(), 45):
                painter.drawLine(x, self.height(), x + 160, 0)
            painter.setBrush(QColor(20, 35, 48, 180))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(self.width() // 2 - 90, 20, 180, 170)
        
        icon_path = "assets/images/icon_camera.png"
        if os.path.exists(icon_path):
            pixmap = QPixmap(icon_path).scaled(68, 68, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            painter.drawPixmap(self.width() // 2 - 34, self.height() // 2 - 34, pixmap)
        else:
            painter.setBrush(QColor("#b995ea" if not self.active else "#741dff"))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(self.width() // 2 - 34, self.height() // 2 - 34, 68, 68)
            painter.setPen(QPen(QColor("#ffffff"), 4))
            cx, cy = self.width() // 2, self.height() // 2
            painter.drawLine(cx - 16, cy - 18, cx - 8, cy - 18)
            painter.drawLine(cx - 18, cy - 16, cx - 18, cy - 8)
            painter.drawLine(cx + 16, cy - 18, cx + 8, cy - 18)
            painter.drawLine(cx + 18, cy - 16, cx + 18, cy - 8)
            painter.drawLine(cx - 16, cy + 18, cx - 8, cy + 18)
            painter.drawLine(cx - 18, cy + 16, cx - 18, cy + 8)
            painter.drawLine(cx + 16, cy + 18, cx + 8, cy + 18)
            painter.drawLine(cx + 18, cy + 16, cx + 18, cy + 8)
        
        painter.setPen(QColor("#777777" if not self.active else "#ffffff"))
        painter.setFont(QFont("Segoe UI", 10))
        text = "Camera Stream Loading...." if not self.active else ""
        painter.drawText(rect.adjusted(0, 90, 0, 0), Qt.AlignCenter, text)


class MainActionButton(QPushButton):
    def __init__(self, text, color="purple", parent=None):
        super().__init__(text, parent)
        self.setObjectName("mainActionButton")
        self.setProperty("buttonColor", color)
        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumSize(150, 82)


class SmallMetricCard(ShadowFrame):
    def __init__(self, title, value, parent=None):
        super().__init__("softCard", parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(0)
        t = QLabel(title)
        t.setAlignment(Qt.AlignCenter)
        t.setStyleSheet("background: transparent; color: #111111; font-size: 16px;")
        v = QLabel(value)
        v.setAlignment(Qt.AlignCenter)
        v.setStyleSheet("background: transparent; color: #7b61ff; font-size: 26px; font-weight: bold;")
        layout.addWidget(t)
        layout.addWidget(v)


class FishThumbnail(QLabel):
    def __init__(self, fish_type="nila", parent=None):
        super().__init__(parent)
        self.setFixedSize(40, 30)
        self.setScaledContents(True)
        
        fish_map = {
            "nila": "assets/images/fish_nila.png",
            "lele": "assets/images/fish_lele.png",
            "mujair": "assets/images/fish_mujair.png",
            "kapal": "assets/images/fish_kapal.png",
        }
        
        img_path = fish_map.get(fish_type.lower(), fish_map["nila"])
        if os.path.exists(img_path):
            pixmap = QPixmap(img_path)
            self.setPixmap(pixmap)
        else:
            self.setStyleSheet(f"background: #cccccc; border-radius: 4px;")
            self.setText("🐟")
            self.setAlignment(Qt.AlignCenter)
