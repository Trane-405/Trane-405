
from database.connection import get_connection

class ProductService:

    def get_by_barcode(self, barcode):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT id,name,price,stock FROM products WHERE barcode=?", (barcode,))
        row = cur.fetchone()

        conn.close()

        if row:
            return {
                "id": row[0],
                "name": row[1],
                "price": row[2],
                "stock": row[3]
            }

        return None

    def add_product(self, name, barcode, price, stock):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO products(name,barcode,price,stock) VALUES (?,?,?,?)",
            (name, barcode, price, stock)
        )

        conn.commit()
        conn.close()
