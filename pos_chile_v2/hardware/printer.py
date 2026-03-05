
def print_ticket(items, total):
    with open("ticket.txt", "w", encoding="utf8") as f:
        f.write("POS CHILE\n")
        f.write("---------------------\n")

        for i in items:
            line = f"{i['name']} x{i['qty']} = {i['price']*i['qty']}"
            f.write(line + "\n")

        f.write("---------------------\n")
        f.write(f"TOTAL: {total}\n")

    print("Ticket generado: ticket.txt")
