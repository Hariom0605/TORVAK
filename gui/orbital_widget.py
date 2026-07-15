"""
TORVAK Orbital Core UI
-----------------------
Drop this file at: gui/orbital_widget.py

Usage in gui/window.py:

    from gui.orbital_widget import OrbitalWidget

    class MainWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.assistant = Assistant()
            self.orbital = OrbitalWidget(on_submit=self.handle_command)
            layout = QVBoxLayout()
            layout.addWidget(self.orbital)
            self.setLayout(layout)
            self.resize(900, 700)

        def handle_command(self, text):
            response = self.assistant.process(text)
            # route to the right node based on which module handled it
            self.orbital.set_active_module("Coding")   # example
            self.orbital.push_event("Coding", response[:40])
            return response
"""

import math
from PySide6.QtWidgets import (
    QWidget, QPushButton, QLineEdit, QLabel,
    QGraphicsDropShadowEffect, QGraphicsOpacityEffect,
)
from PySide6.QtCore import (
    Qt, QTimer, QPropertyAnimation, QEasingCurve, QPointF, QRectF, Property,
)
from PySide6.QtGui import (
    QPainter, QPainterPath, QRadialGradient, QColor, QFont, QBrush, QPen,
)

# ---------------------------------------------------------------------------
# Palette — deep black base, crimson accent
# ---------------------------------------------------------------------------
BG = QColor("#0b0a0a")
ACCENT_LIGHT = QColor("#f7b3b5")
ACCENT_MID = QColor("#c23c42")
ACCENT_DARK = QColor("#4a1215")
NODE_IDLE_BORDER = QColor("#2e2626")
NODE_IDLE_ICON = QColor("#78706f")
TEXT_MUTED = QColor("#6e6664")
TEXT_MAIN = QColor("#ece7e6")

MODULES = [
    ("Memory", "\uf4b3"),   # placeholder icons — swap for a real icon font in production
    ("Voice", "\uf130"),
    ("Vision", "\uf06e"),
    ("Coding", "\uf121"),
    ("Web", "\uf0ac"),
    ("System", "\uf085"),
]


# ---------------------------------------------------------------------------
# Central morphing core
# ---------------------------------------------------------------------------
class CoreBlob(QWidget):
    """A soft organic blob that continuously breathes/morphs — the 'living' core."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(180, 180)
        self._t = 0.0
        self._points = 8
        self._base_radius = 58.0
        self._pulse_scale = 1.0

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)
        self._timer.start(33)  # ~30fps, smooth without hogging CPU

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(46)
        shadow.setColor(QColor(160, 40, 45, 150))
        shadow.setOffset(0, 14)
        self.setGraphicsEffect(shadow)
        self._shadow = shadow

    def _tick(self):
        self._t += 0.02
        self.update()

    def pulse(self):
        """Call this when the core 'thinks' — smooth scale-up and settle."""
        anim = QPropertyAnimation(self, b"pulseScale", self)
        anim.setDuration(500)
        anim.setEasingCurve(QEasingCurve.OutBack)
        anim.setStartValue(1.0)
        anim.setKeyValueAt(0.4, 1.12)
        anim.setEndValue(1.0)
        anim.start(QPropertyAnimation.DeleteWhenStopped)
        self._pulse_anim = anim

    def getPulseScale(self):
        return self._pulse_scale

    def setPulseScale(self, v):
        self._pulse_scale = v
        self.update()

    pulseScale = Property(float, getPulseScale, setPulseScale)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        cx, cy = self.width() / 2, self.height() / 2
        radius = self._base_radius * self._pulse_scale

        path = QPainterPath()
        coords = []
        for i in range(self._points):
            ang = (i / self._points) * 2 * math.pi
            r = radius + math.sin(self._t + i * 1.3) * 9 + math.cos(self._t * 0.7 + i) * 5
            coords.append((cx + math.cos(ang) * r, cy + math.sin(ang) * r))

        path.moveTo(coords[0][0], coords[0][1])
        for i in range(self._points):
            c = coords[i]
            n = coords[(i + 1) % self._points]
            mx, my = (c[0] + n[0]) / 2, (c[1] + n[1]) / 2
            path.quadTo(c[0], c[1], mx, my)
        path.closeSubpath()

        grad = QRadialGradient(cx - 20, cy - 25, radius * 1.5)
        grad.setColorAt(0.0, ACCENT_LIGHT)
        grad.setColorAt(0.45, ACCENT_MID)
        grad.setColorAt(1.0, ACCENT_DARK)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(grad))
        painter.drawPath(path)

        # glossy highlight, gives it a glassy/3D feel
        hl = QRadialGradient(cx - 22, cy - 30, 28)
        hl.setColorAt(0.0, QColor(255, 255, 255, 150))
        hl.setColorAt(1.0, QColor(255, 255, 255, 0))
        painter.setBrush(QBrush(hl))
        painter.drawEllipse(QPointF(cx - 22, cy - 30), 26, 15)


# ---------------------------------------------------------------------------
# Orbiting module node
# ---------------------------------------------------------------------------
class OrbitNode(QPushButton):
    """A circular module button. Lift + glow smoothly when active — the '3D' cue."""

    SIZE = 52

    def __init__(self, label, glyph, parent=None):
        super().__init__(parent)
        self.label = label
        self.setFixedSize(self.SIZE, self.SIZE)
        self.setCursor(Qt.PointingHandCursor)
        self.setText(glyph)
        self.setFont(QFont("Segoe UI", 15))
        self._active = False

        self._shadow = QGraphicsDropShadowEffect(self)
        self._shadow.setBlurRadius(10)
        self._shadow.setColor(QColor(0, 0, 0, 130))
        self._shadow.setOffset(0, 5)
        self.setGraphicsEffect(self._shadow)

        self._blur_anim = QPropertyAnimation(self._shadow, b"blurRadius", self)
        self._blur_anim.setDuration(380)
        self._blur_anim.setEasingCurve(QEasingCurve.OutCubic)

        self._geo_anim = QPropertyAnimation(self, b"geometry", self)
        self._geo_anim.setDuration(380)
        self._geo_anim.setEasingCurve(QEasingCurve.OutCubic)

        self._apply_style()

    def _apply_style(self):
        if self._active:
            self.setStyleSheet(f"""
                QPushButton {{
                    background: qlineargradient(x1:0,y1:0,x2:1,y2:1,
                        stop:0 #332020, stop:1 #1c1010);
                    border: 1px solid {ACCENT_MID.name()};
                    border-radius: {self.SIZE // 2}px;
                    color: {ACCENT_LIGHT.name()};
                }}
            """)
        else:
            self.setStyleSheet(f"""
                QPushButton {{
                    background: qlineargradient(x1:0,y1:0,x2:1,y2:1,
                        stop:0 #1c1717, stop:1 #111010);
                    border: 1px solid {NODE_IDLE_BORDER.name()};
                    border-radius: {self.SIZE // 2}px;
                    color: {NODE_IDLE_ICON.name()};
                }}
            """)

    def set_active(self, active: bool, animate: bool = True):
        if self._active == active:
            return
        self._active = active
        self._apply_style()
        self._shadow.setColor(QColor(194, 60, 66, 190) if active else QColor(0, 0, 0, 130))

        # smooth glow lift
        self._blur_anim.stop()
        self._blur_anim.setStartValue(self._shadow.blurRadius())
        self._blur_anim.setEndValue(26 if active else 10)
        self._blur_anim.start()

        if animate:
            # subtle 3D "lift" — grow by a few px around its own center, ease back
            cur = self.geometry()
            grow = 6 if active else -6
            target = QRectF(
                cur.x() - grow / 2, cur.y() - grow / 2,
                cur.width() + grow, cur.height() + grow
            ).toRect()
            self._geo_anim.stop()
            self._geo_anim.setStartValue(cur)
            self._geo_anim.setEndValue(target)
            self._geo_anim.start()


# ---------------------------------------------------------------------------
# Ephemeral activity chip (replaces a chat/timeline list)
# ---------------------------------------------------------------------------
class ActivityChip(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet(f"""
            QLabel {{
                background: rgba(255,255,255,12);
                border: 1px solid rgba(255,255,255,20);
                border-radius: 14px;
                padding: 6px 12px;
                color: #d1c9c8;
                font-size: 11px;
            }}
        """)
        self.adjustSize()

        self._effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self._effect)
        self._effect.setOpacity(0.0)

        self._in = QPropertyAnimation(self._effect, b"opacity", self)
        self._in.setDuration(300)
        self._in.setStartValue(0.0)
        self._in.setEndValue(1.0)
        self._in.setEasingCurve(QEasingCurve.OutCubic)

        self._out = QPropertyAnimation(self._effect, b"opacity", self)
        self._out.setDuration(500)
        self._out.setStartValue(1.0)
        self._out.setEndValue(0.0)
        self._out.setEasingCurve(QEasingCurve.InCubic)

        self.show()
        self._in.start()
        QTimer.singleShot(2600, self._fade_out)

    def _fade_out(self):
        self._out.finished.connect(self.deleteLater)
        self._out.start()


# ---------------------------------------------------------------------------
# Floating glass command dock
# ---------------------------------------------------------------------------
class CommandDock(QWidget):
    def __init__(self, on_submit, parent=None):
        super().__init__(parent)
        self._on_submit = on_submit
        self.setFixedHeight(48)
        self.setStyleSheet(f"""
            CommandDock {{
                background: rgba(255,255,255,9);
                border: 1px solid rgba(255,255,255,18);
                border-radius: 24px;
            }}
        """)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setColor(QColor(0, 0, 0, 140))
        shadow.setOffset(0, 10)
        self.setGraphicsEffect(shadow)

        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Say something to TORVAK...")
        self.input.setStyleSheet(f"""
            QLineEdit {{
                background: transparent;
                border: none;
                color: {TEXT_MAIN.name()};
                font-size: 14px;
            }}
        """)
        self.input.returnPressed.connect(self._submit)

        self.send_btn = QPushButton("\u2191", self)
        self.send_btn.setFixedSize(36, 36)
        self.send_btn.setCursor(Qt.PointingHandCursor)
        self.send_btn.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1:0,y1:0,x2:1,y2:1,
                    stop:0 {ACCENT_LIGHT.name()}, stop:1 {ACCENT_MID.name()});
                border: none;
                border-radius: 18px;
                color: #1c0708;
                font-weight: bold;
            }}
        """)
        self.send_btn.clicked.connect(self._submit)

    def _submit(self):
        text = self.input.text().strip()
        if not text:
            return
        self.input.clear()
        if self._on_submit:
            self._on_submit(text)

    def resizeEvent(self, event):
        pad = 8
        self.send_btn.move(self.width() - self.send_btn.width() - pad,
                            (self.height() - self.send_btn.height()) // 2)
        self.input.setGeometry(18, 0, self.width() - self.send_btn.width() - pad - 30, self.height())
        super().resizeEvent(event)


# ---------------------------------------------------------------------------
# Main orbital widget — assembles core + nodes + rings + dock + chips
# ---------------------------------------------------------------------------
class OrbitalWidget(QWidget):
    RING_OUTER = 380
    RING_INNER = 280
    ORBIT_RADIUS = 165

    def __init__(self, on_submit=None, parent=None):
        super().__init__(parent)
        self.setStyleSheet(f"background: {BG.name()};")
        self.setMinimumSize(700, 640)

        self.title = QLabel("T O R V A K", self)
        self.title.setStyleSheet(f"color: {TEXT_MUTED.name()}; font-size: 11px; letter-spacing: 4px;")

        self.status_core = QLabel("98% core", self)
        self.status_core.setStyleSheet(f"color: {ACCENT_MID.name()}; font-size: 12px;")
        self.status_time = QLabel("--:--", self)
        self.status_time.setStyleSheet(f"color: {TEXT_MUTED.name()}; font-size: 12px;")

        self.core = CoreBlob(self)

        self.nodes = {}
        for label, glyph in MODULES:
            node = OrbitNode(label, glyph, self)
            node.clicked.connect(lambda _, l=label: self.set_active_module(l, user_triggered=True))
            self.nodes[label] = node

        self.dock = CommandDock(on_submit=self._handle_submit, parent=self)
        self._on_submit_cb = on_submit

        self._active_module = None
        self._chip_container = self  # chips are placed directly on self

        # clock
        self._clock_timer = QTimer(self)
        self._clock_timer.timeout.connect(self._update_clock)
        self._clock_timer.start(1000)
        self._update_clock()

    def _update_clock(self):
        from datetime import datetime
        self.status_time.setText(datetime.now().strftime("%H:%M"))

    def _handle_submit(self, text):
        self.core.pulse()
        if self._on_submit_cb:
            self._on_submit_cb(text)

    # ---- public API -----------------------------------------------------
    def set_active_module(self, label, user_triggered=False):
        """Call this from your command router when a module handles a request."""
        if label not in self.nodes:
            return
        if self._active_module and self._active_module in self.nodes:
            self.nodes[self._active_module].set_active(False)
        self.nodes[label].set_active(True)
        self._active_module = label
        self.core.pulse()
        if user_triggered:
            self.push_event(label, "activated")

    def push_event(self, label, message):
        """Show a small fading chip near the given module's node."""
        if label not in self.nodes:
            return
        node = self.nodes[label]
        chip = ActivityChip(f"{label} — {message}", self)
        cx = node.x() + node.width() // 2
        cy = node.y() + node.height() // 2
        dx = 1 if cx > self.width() / 2 else -1
        chip.move(min(max(cx + dx * 40 - chip.width() // 2, 8), self.width() - chip.width() - 8),
                  max(cy - 60, 8))
        chip.show()

    # ---- layout -----------------------------------------------------------
    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        cx, cy = w / 2, h * 0.44

        self.title.move(24, 20)
        self.status_time.move(w - 90, 20)
        self.status_core.move(w - 180, 20)

        self.core.move(int(cx - self.core.width() / 2), int(cy - self.core.height() / 2))

        n = len(MODULES)
        for i, (label, _) in enumerate(MODULES):
            ang = (i / n) * 2 * math.pi - math.pi / 2
            nx = cx + math.cos(ang) * self.ORBIT_RADIUS
            ny = cy + math.sin(ang) * self.ORBIT_RADIUS
            node = self.nodes[label]
            node.move(int(nx - node.width() / 2), int(ny - node.height() / 2))

        dock_w = min(420, w - 60)
        self.dock.setGeometry(int(cx - dock_w / 2), h - 70, dock_w, 48)

        super().resizeEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        cx, cy = self.width() / 2, self.height() * 0.44

        pen = QPen(QColor(255, 255, 255, 15))
        pen.setWidthF(0.6)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(QPointF(cx, cy), self.RING_OUTER / 2, self.RING_OUTER / 2)
        painter.drawEllipse(QPointF(cx, cy), self.RING_INNER / 2, self.RING_INNER / 2)

        # ambient glow behind the core
        glow = QRadialGradient(cx, cy, 260)
        glow.setColorAt(0.0, QColor(190, 50, 55, 18))
        glow.setColorAt(1.0, QColor(190, 50, 55, 0))
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(glow))
        painter.drawEllipse(QPointF(cx, cy), 260, 260)

        super().paintEvent(event)
