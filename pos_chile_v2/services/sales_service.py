
from database.connection import get_connection

class SalesService:

    def create_sale(self, items):
        conn = get_connection()
        cur = conn.cursor()

        total = sum(i["price"] * i["qty"] for i in items)

        cur.execute("INSERT INTO sales(total) VALUES(?)", (total,))
        sale_id = cur.lastrowid

        for i in items:
            cur.execute(
                "INSERT INTO sale_items(sale_id,product_id,quantity,price) VALUES (?,?,?,?)",
                (sale_id, i["id"], i["qty"], i["price"])
            )

            cur.execute(
                "UPDATE products SET stock = stock - ? WHERE id=?",
                (i["qty"], i["id"])
            )

        conn.commit()
        conn.close()

        return sale_id, total
