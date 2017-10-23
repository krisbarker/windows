#! python3

# This should be a script that creates
# A simple windows interface for running the
# volume checker for the oil tank

import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(450, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
