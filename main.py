import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400,300)
        self.setWindowTitle("Популярно")
        self.init_ui()

    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout() 
        layout.setSpacing(10)

        self.label = QLabel("Текст: ")

        self.input = QLineEdit()
        self.input.setPlaceholderText("Текст")
        
        self.btn = QPushButton("Текст")
        self.bt4 = QPushButton("Выйти")
        self.btn.clicked.connect(self.btn_text)
        self.bt4.clicked.connect(self.close)


        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.btn)
        layout.addWidget(self.bt4)
        central.setLayout(layout)

    def btn_text(self):
        text = self.input.text()
        self.label.setText(f"Текст: {text}")
    def btn_delete(self):
        pass
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = MainWindow()
    m.show()
    sys.exit(app.exec())
