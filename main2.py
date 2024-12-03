import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QComboBox, QMessageBox


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


class SortingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.sorting_algorithms = SortingAlgorithms()

        self.setWindowTitle("Тренажер сортировки")
        self.setGeometry(100, 100, 400, 400)

        self.layout = QVBoxLayout()

        self.label = QLabel("Введите массив чисел через пробел:")
        self.layout.addWidget(self.label)

        self.entry_array = QLineEdit()
        self.layout.addWidget(self.entry_array)

        self.sorting_label = QLabel("Выберите метод сортировки:")
        self.layout.addWidget(self.sorting_label)

        self.sorting_var = QComboBox()
        self.sorting_var.addItems([
            "Bubble Sort",
            "Selection Sort",
            "Insertion Sort",
            "Quick Sort",
            "Merge Sort"
        ])
        self.layout.addWidget(self.sorting_var)

        self.sort_button = QPushButton("Сортировать")
        self.sort_button.clicked.connect(self.sort_array)
        self.layout.addWidget(self.sort_button)

        self.description_label = QLabel("Описание алгоритма:")
        self.layout.addWidget(self.description_label)

        self.result_label = QLabel("Отсортированный массив:")
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def sort_array(self):
        try:
            arr = list(map(int, self.entry_array.text().split()))
            sorting_mode = self.sorting_var.currentText()

            descriptions = {
                "Bubble Sort": "Пузырьковая сортировка сравнивает элементы попарно, меняя их местами, если порядок неверный.",
                "Selection Sort": "Выбор самой маленькой величины для каждой позиции из неотсортированной части массива.",
                "Insertion Sort": "Каждый элемент вставляется в нужное место отсортированной части массива.",
                "Quick Sort": "Элементы делятся на две группы вокруг опорного элемента, затем сортируются рекурсивно.",
                "Merge Sort": "Массив делится на части, сортируется и объединяется обратно."
            }

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

            self.description_label.setText("Описание алгоритма: " + descriptions[sorting_mode])
            self.result_label.setText("Отсортированный массив: " + ' '.join(map(str, sorted_arr)))
        except ValueError:
            QMessageBox.critical(self, "Error", "Введите массив чисел через пробел")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SortingApp()
    window.show()
    sys.exit(app.exec())
