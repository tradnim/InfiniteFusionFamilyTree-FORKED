from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QLabel, QWidget, QGridLayout

class StarOverlayWidget(QWidget):
    """A star-shaped overlay that can be added to sprite widgets to indicate custom sprites"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Create star label with transparent background
        self.star_label = QLabel()
        self.star_label.setStyleSheet("""
            QLabel {
                color: #FFD700; /* Gold color */
                font-size: 18px;
                font-weight: bold;
                background: transparent;
            }
        """)
        self.star_label.setText("★")
        
        # Use grid layout for precise positioning
        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.star_label, 0, 0, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)
        
        # Make widget background transparent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def adjustSize(self, parent_size):
        """Adjust overlay size to match parent widget while keeping star in corner"""
        self.setFixedSize(parent_size)
        star_size = min(parent_size.width(), parent_size.height()) // 5
        self.star_label.setFixedSize(QSize(star_size, star_size))