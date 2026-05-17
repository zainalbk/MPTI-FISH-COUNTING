from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainter, QColor, QPen, QFont
from PyQt5.QtWidgets import QWidget


class BarChart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._labels = ["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"]
        self._values = [800, 950, 720, 1100, 890, 650, 780]
        self.setMinimumHeight(280)

    def set_data(self, labels, values):
        self._labels = labels
        self._values = values
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        w = self.width()
        h = self.height()
        margin = 40
        chart_h = h - margin * 2

        if not self._values:
            return

        max_val = max(self._values) if self._values else 1
        bar_width = (w - margin * 2) / len(self._values) * 0.7
        spacing = (w - margin * 2) / len(self._values)

        for i, val in enumerate(self._values):
            bar_h = (val / max_val) * chart_h
            x = margin + i * spacing + (spacing - bar_width) / 2
            y = h - margin - bar_h

            painter.fillRect(int(x), int(y), int(bar_width), int(bar_h), QColor("#9d7bff"))

            painter.setPen(QColor("#bfb7d8"))
            font = QFont("Arial", 9)
            painter.setFont(font)
            label = self._labels[i] if i < len(self._labels) else str(i)
            painter.drawText(int(x), h - margin + 20, int(bar_width), 20, Qt.AlignCenter, label)


class LineChart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._values = [500, 620, 580, 700, 850, 920, 880, 950, 1020, 980, 1100, 1050]
        self.setMinimumHeight(280)

    def set_data(self, values):
        self._values = values
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        w = self.width()
        h = self.height()
        margin = 40
        chart_h = h - margin * 2
        chart_w = w - margin * 2

        if len(self._values) < 2:
            return

        max_val = max(self._values) if self._values else 1
        step_x = chart_w / (len(self._values) - 1)

        pen = QPen(QColor("#9d7bff"), 3)
        painter.setPen(pen)

        for i in range(len(self._values) - 1):
            x1 = margin + i * step_x
            y1 = h - margin - (self._values[i] / max_val) * chart_h
            x2 = margin + (i + 1) * step_x
            y2 = h - margin - (self._values[i + 1] / max_val) * chart_h
            painter.drawLine(int(x1), int(y1), int(x2), int(y2))

        painter.setBrush(QColor("#9d7bff"))
        for i, val in enumerate(self._values):
            x = margin + i * step_x
            y = h - margin - (val / max_val) * chart_h
            painter.drawEllipse(int(x - 4), int(y - 4), 8, 8)


class PieChart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._data = {"Sehat": 70, "Rusak": 20, "Perlu Cek": 10}
        self._colors = {"Sehat": "#9d7bff", "Rusak": "#ff6b9d", "Perlu Cek": "#ffa726"}
        self.setMinimumSize(280, 280)

    def set_data(self, data_dict):
        self._data = data_dict
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        w = self.width()
        h = self.height()
        size = min(w, h) - 80
        rect = QRectF((w - size) / 2, (h - size) / 2, size, size)

        total = sum(self._data.values())
        if total == 0:
            return

        start_angle = 0
        for label, value in self._data.items():
            span = int((value / total) * 360 * 16)
            color = self._colors.get(label, "#888888")
            painter.setBrush(QColor(color))
            painter.setPen(Qt.NoPen)
            painter.drawPie(rect, start_angle, span)
            start_angle += span

        legend_y = h - 60
        legend_x = 20
        painter.setFont(QFont("Arial", 9))
        for label, value in self._data.items():
            color = self._colors.get(label, "#888888")
            painter.fillRect(legend_x, legend_y, 16, 16, QColor(color))
            painter.setPen(QColor("#bfb7d8"))
            painter.drawText(legend_x + 22, legend_y + 12, f"{label}: {value}%")
            legend_x += 140
