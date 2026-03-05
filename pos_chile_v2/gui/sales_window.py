
from PyQt6.QtWidgets import QWidget,QVBoxLayout,QLineEdit,QPushButton,QListWidget
from services.product_service import ProductService
from services.sales_service import SalesService
from hardware.printer import print_ticket

class SalesWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.products=[]
        self.product_service=ProductService()
        self.sales_service=SalesService()

        layout=QVBoxLayout()

        self.barcode_input=QLineEdit()
        self.barcode_input.setPlaceholderText("Escanear codigo de barras")
        self.barcode_input.returnPressed.connect(self.add_product)

        self.list=QListWidget()

        btn_pay=QPushButton("Cobrar")
        btn_pay.clicked.connect(self.pay)

        layout.addWidget(self.barcode_input)
        layout.addWidget(self.list)
        layout.addWidget(btn_pay)

        self.setLayout(layout)

    def add_product(self):
        code=self.barcode_input.text()
        product=self.product_service.get_by_barcode(code)

        if product:
            product["qty"]=1
            self.products.append(product)
            self.list.addItem(product["name"])

        self.barcode_input.clear()

    def pay(self):
        sale_id,total=self.sales_service.create_sale(self.products)
        print_ticket(self.products,total)

        self.products=[]
        self.list.clear()
