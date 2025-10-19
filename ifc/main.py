import sys
import os

# When running this file directly (python ifc/main.py) Python sets
# sys.path[0] to the `ifc` directory which prevents absolute imports
# like `import ifc` from working. Ensure the project root is on sys.path
# so absolute imports resolve whether the module is run directly or via -m.
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from PyQt6.QtWidgets import QApplication
from ifc.gui.window import IFCWindow


def main():
    app = QApplication([])
    window = IFCWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
