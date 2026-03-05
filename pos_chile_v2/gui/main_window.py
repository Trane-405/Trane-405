
from PyQt6.QtWidgets import QMainWindow,QPushButton,QVBoxLayout,QWidget
from gui.sales_window import SalesWindow
from gui.inventory_window import InventoryWindow
from reports.excel_report import export_sales_excel

class MainWindow(QMainWindow):

    def __init__(self,user):
        super().__init__()

        self.setWindowTitle("POS CHILE V2")

        layout=QVBoxLayout()

        btn_sales=QPushButton("Ventas")
        btn_sales.clicked.connect(self.open_sales)

        btn_inventory=QPushButton("Inventario")
        btn_inventory.clicked.connect(self.open_inventory)

        btn_report=QPushButton("Exportar ventas Excel")
        btn_report.clicked.connect(export_sales_excel)

        layout.addWidget(btn_sales)
        layout.addWidget(btn_inventory)
        layout.addWidget(btn_report)

        container=QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def open_sales(self):
        self.sales=SalesWindow()
        self.sales.show()

    def open_inventory(self):
        self.inv=InventoryWindow()
        self.inv.show()
