
from database.connection import get_connection
from openpyxl import Workbook

def export_sales_excel():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id,total,date FROM sales")
    rows = cur.fetchall()

    wb = Workbook()
    ws = wb.active
    ws.append(["ID","Total","Fecha"])

    for r in rows:
        ws.append(r)

    wb.save("ventas.xlsx")
    conn.close()

    print("Reporte Excel generado")
