import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.btn.clicked.connect(self.func)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта',
                                                                     'степень обжарки', 'молотый/в зернах',
                                                                     'описание вкуса', 'цена', 'объем упаковки'])
        self.tableWidget.resizeColumnsToContents()

    def func(self):
        name = self.name.text()
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        data = cur.execute(f'SELECT * FROM data WHERE name = ?', (name,)).fetchall()
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())