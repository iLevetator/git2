import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.uic.properties import QtGui


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.move(600, 300)
        self.load_table()
        self.load_editor()

    def load_table(self):
        with sqlite3.connect('coffee.sqlite') as con:
            res = con.cursor().execute("SELECT * FROM coffee").fetchall()
        self.n = len(res)
        self.table.setColumnCount(7)
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(('ID', 'grade', 'roasting',
                                              'is_ground', 'taste', 'price', 'volume'))
        for i, row in enumerate(res):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(elem)))
        self.table.resizeColumnsToContents()
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                self.table.item(i, j).setFlags(self.table.item(i, j).flags() ^ Qt.ItemIsEditable)

    def load_editor(self):
        self.next = Editor(self.n)

    def closeEvent(self, *args):
        self.next.close()


class Editor(QMainWindow):
    def __init__(self, n):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.ID.setMaximum(n)
        self.n = n
        self.btn_new.clicked.connect(self.new)
        self.btn_load.clicked.connect(self.load)
        self.btn_edit.clicked.connect(self.edit)
        self.show()
        self.move(1100, 300)
        self.table.setColumnCount(7)
        self.table.setRowCount(1)
        self.table.setHorizontalHeaderLabels(('ID', 'grade', 'roasting',
                                              'is_ground', 'taste', 'price', 'volume'))
        self.table.resizeColumnsToContents()
        self.new()

    def new(self):
        self.current = ('',) * 7
        for j, elem in enumerate(self.current):
            self.table.setItem(0, j, QTableWidgetItem(str(elem)))

    def load(self):
        with sqlite3.connect('coffee.sqlite') as con:
            self.n = len(con.cursor().execute("SELECT * FROM coffee").fetchall())
            self.ID.setMaximum(self.n)
            self.current = con.cursor().execute("SELECT * FROM coffee WHERE ID = ?",
                                                (self.ID.value(),)).fetchone()
        for j, elem in enumerate(self.current):
            self.table.setItem(0, j, QTableWidgetItem(str(elem)))
        self.table.resizeColumnsToContents()

    def edit(self):
        self.current = tuple(self.table.item(0, i).text() for i in range(7))
        with sqlite3.connect('coffee.sqlite') as con:
            if int(self.current[0]) > self.n:
                print(self.current[1:])
                con.cursor().execute("INSERT INTO coffee(ID, grade, roasting, is_ground, "
                                     "taste, price, volume) VALUES(?, ?, ?, ?, ?, ?, ?)",
                                     self.current)
            for i in range(1, 7):
                print((self.table.horizontalHeaderItem(i).text(), self.current[i], i))
                con.cursor().execute(f"UPDATE coffee SET {self.table.horizontalHeaderItem(i).text()}"
                                     f" = ? WHERE ID = ?", (self.current[i], self.current[0]))
        self.table.resizeColumnsToContents()
        ex.load_table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
