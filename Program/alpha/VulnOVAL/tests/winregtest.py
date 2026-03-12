import sys
from PySide6.QtCore import QEvent, QPropertyAnimation, QEasingCurve, QRect
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QFrame


class EdgeReveal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edge hover reveal (PySide6)")
        self.setMouseTracking(True)

        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)

        # Панель слева
        self.panel = QFrame()
        self.panel.setFrameShape(QFrame.StyledPanel)
        self.panel_layout = QVBoxLayout(self.panel)
        self.panel_layout.addWidget(QLabel("Меню"))
        self.panel_layout.addWidget(QPushButton("Пункт 1"))
        self.panel_layout.addWidget(QPushButton("Пункт 2"))
        self.panel_layout.addStretch(1)

        self.panel_full_width = 220
        self.panel.setMaximumWidth(0)  # старт: скрыто

        # Контент
        content = QWidget()
        cl = QVBoxLayout(content)
        cl.addWidget(QLabel("<h2>Контент</h2>"))
        cl.addWidget(QLabel("Подведи мышь к ЛЕВОМУ краю окна — панель выедет."))
        cl.addStretch(1)

        root.addWidget(self.panel)
        root.addWidget(content, 1)

        # Анимация ширины панели
        self.anim = QPropertyAnimation(self.panel, b"maximumWidth", self)
        self.anim.setDuration(220)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)

        # чтобы ловить движения мыши даже над дочерними виджетами
        QApplication.instance().installEventFilter(self)

        self._opened = False
        self.edge_px = 8  # "горячая" зона у левого края

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseMove:
            p = self.mapFromGlobal(event.globalPosition().toPoint())
            inside = QRect(0, 0, self.width(), self.height()).contains(p)

            if inside:
                # если мышь у левого края — открыть
                if p.x() <= self.edge_px:
                    self.open_panel()
                # если панель открыта и мышь далеко от панели — закрыть
                elif self._opened and p.x() > self.panel_full_width + 40:
                    self.close_panel()

        elif event.type() == QEvent.Leave:
            # иногда полезно закрывать при уходе мыши с окна
            # self.close_panel()
            pass

        return super().eventFilter(obj, event)

    def open_panel(self):
        if self._opened:
            return
        self._opened = True
        self.anim.stop()
        self.anim.setStartValue(self.panel.maximumWidth())
        self.anim.setEndValue(self.panel_full_width)
        self.anim.start()

    def close_panel(self):
        if not self._opened:
            return
        self._opened = False
        self.anim.stop()
        self.anim.setStartValue(self.panel.maximumWidth())
        self.anim.setEndValue(0)
        self.anim.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = EdgeReveal()
    w.resize(720, 420)
    w.show()
    sys.exit(app.exec())
