import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 9 - QDialog, QTabWidget, & MenuBar")
        self.setGeometry(100, 100, 600, 400)

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        exit_action = QAction("Keluar", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        fitur_menu = menu_bar.addMenu("Fitur")

        fitur_input = QAction("Input Nama", self)
        fitur_input.triggered.connect(lambda: self.tab_widget.setCurrentIndex(0))

        fitur_font = QAction("Pilih Font", self)
        fitur_font.triggered.connect(lambda: self.tab_widget.setCurrentIndex(1))

        fitur_file = QAction("Buka File", self)
        fitur_file.triggered.connect(lambda: self.tab_widget.setCurrentIndex(2))

        fitur_menu.addAction(fitur_input)
        fitur_menu.addAction(fitur_font)
        fitur_menu.addAction(fitur_file)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.North)

        self.tab1 = QWidget()
        self.tab1_layout = QVBoxLayout()
        self.name_label = QLabel("No name entered")
        self.name_label.setAlignment(Qt.AlignCenter)
        self.name_button = QPushButton("Input Nama")
        self.name_button.clicked.connect(self.input_name)
        self.tab1_layout.addWidget(self.name_button)
        self.tab1_layout.addWidget(self.name_label)
        self.tab1.setLayout(self.tab1_layout)
        self.tab_widget.addTab(self.tab1, "Input Nama")

        self.tab2 = QWidget()
        self.tab2_layout = QVBoxLayout()
        self.font_label = QLabel("Select a font")
        self.font_label.setAlignment(Qt.AlignCenter)
        self.font_button = QPushButton("Pilih Font")
        self.font_button.clicked.connect(self.choose_font)
        self.tab2_layout.addWidget(self.font_button)
        self.tab2_layout.addWidget(self.font_label)
        self.tab2.setLayout(self.tab2_layout)
        self.tab_widget.addTab(self.tab2, "Pilih Font")

        self.tab3 = QWidget()
        self.tab3_layout = QVBoxLayout()
        self.file_button = QPushButton("Buka File .txt")
        self.file_button.clicked.connect(self.open_file)
        self.file_text = QTextEdit()
        self.file_text.setReadOnly(True)
        self.tab3_layout.addWidget(self.file_button)
        self.tab3_layout.addWidget(self.file_text)
        self.tab3.setLayout(self.tab3_layout)
        self.tab_widget.addTab(self.tab3, "Buka File")

        main_layout.addWidget(self.tab_widget)

    def input_name(self):
        name, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name:")
        if ok and name:
            self.name_label.setText(f"Name: {name}")

    def choose_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.font_label.setText(f"Selected Font: {font.family()}")
            self.font_label.setFont(font)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", 
                                                 "Text Files (*.txt);;All Files (*)")
        if file_name:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.file_text.setPlainText(content)
            except Exception as e:
                self.file_text.setPlainText(f"Error reading file: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())