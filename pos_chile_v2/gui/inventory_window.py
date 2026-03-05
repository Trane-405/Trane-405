
from PyQt6.QtWidgets import QWidget,QVBoxLayout,QLineEdit,QPushButton
from services.product_service import ProductService

class InventoryWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.service=ProductService()

        layout=QVBoxLayout()

        self.name=QLineEdit()
        self.name.setPlaceholderText("Nombre producto")

        self.barcode=QLineEdit()
        self.barcode.setPlaceholderText("Codigo barra")

        self.price=QLineEdit()
        self.price.setPlaceholderText("Precio")

        self.stock=QLineEdit()
        self.stock.setPlaceholderText("Stock")

        btn=QPushButton("Guardar")
        btn.clicked.connect(self.save)

        layout.addWidget(self.name)
        layout.addWidget(self.barcode)
        layout.addWidget(self.price)
        layout.addWidget(self.stock)
        layout.addWidget(btn)

        self.setLayout(layout)

    def save(self):
        self.service.add_product(
            self.name.text(),
            self.barcode.text(),
            float(self.price.text()),
            int(self.stock.text())
        )

        self.name.clear()
        self.barcode.clear()
        self.price.clear()
        self.stock.clear()
