# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget, QMessageBox)

class SortingAlgorithms:
    def __init__(self):
        pass

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return self.quick_sort(less) + [pivot] + self.quick_sort(greater)

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(507, 444)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.verticalLayout.addWidget(self.textEdit_2)

        self.sorting_var = QComboBox(self.centralwidget)
        self.sorting_var.addItems([
            "Bubble Sort",
            "Selection Sort",
            "Insertion Sort",
            "Quick Sort",
            "Merge Sort"
        ])

        self.sorting_var.setObjectName(u"sorting_var")

        self.verticalLayout.addWidget(self.sorting_var)

        self.sort_button = QPushButton(self.centralwidget)
        self.sort_button.setObjectName(u"sort_button")

        self.verticalLayout.addWidget(self.sort_button)

        self.entry_array = QLabel(self.centralwidget)
        self.entry_array.setObjectName(u"entry_array")

        self.verticalLayout.addWidget(self.entry_array)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 507, 31))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.sort_button.clicked.connect(self.sort_array)

    # setupUi

    def sort_array(self):
        try:
            arr = list(map(int, self.entry_array.text().split()))
            sorting_mode = self.sorting_var.currentText()

            if sorting_mode == "Bubble Sort":
                sorted_arr = self.sorting_algorithms.bubble_sort(arr.copy())
            elif sorting_mode == "Selection Sort":
                sorted_arr = self.sorting_algorithms.selection_sort(arr.copy())
            elif sorting_mode == "Insertion Sort":
                sorted_arr = self.sorting_algorithms.insertion_sort(arr.copy())
            elif sorting_mode == "Quick Sort":
                sorted_arr = self.sorting_algorithms.quick_sort(arr.copy())
            elif sorting_mode == "Merge Sort":
                sorted_arr = self.sorting_algorithms.merge_sort(arr.copy())
            else:
                QMessageBox.critical(self, "Error", "Выберите метод сортировки")
                return

            self.result_entry_array.setText("Отсортированный массив: " + ' '.join(map(str, sorted_arr)))
        except ValueError:
            QMessageBox.critical(self, "Error", "Введите массив чисел через пробел")
            
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-style:italic; color:#ffaa7f;\">\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043c\u0430\u0441\u0441\u0438\u0432 \u0447\u0438\u0441\u0435\u043b \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-style:italic; color:#ffaa7f;\"><br /></p></body></html>", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-style:italic; color:#bd7e5e;\">\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u0435\u0442\u043e\u0434 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438:</span></p></body></html>", None))
        self.sorting_var.setItemText(0, QCoreApplication.translate("MainWindow", u"Bubble Sort", None))
        self.sorting_var.setItemText(1, QCoreApplication.translate("MainWindow", u"Selection Sort", None))
        self.sorting_var.setItemText(2, QCoreApplication.translate("MainWindow", u"Insertion Sort", None))
        self.sorting_var.setItemText(3, QCoreApplication.translate("MainWindow", u"Quick Sort", None))
        self.sorting_var.setItemText(4, QCoreApplication.translate("MainWindow", u"Merge Sort", None))

        self.sort_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.entry_array.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u043c\u0430\u0441\u0441\u0438\u0432:", None))
    # retranslateUi

