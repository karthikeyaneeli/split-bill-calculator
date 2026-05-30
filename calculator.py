def calculate_splits(people, expenses):
    if not people or not expenses:
        return [], 0

    total = sum(e["amount"] for e in expenses)
    share = total / len(people)

    balance = {p: 0.0 for p in people}
    for e in expenses:
        balance[e["paid_by"]] += e["amount"]
    for p in people:
        balance[p] -= share

    debtors = sorted([(p, -b) for p, b in balance.items() if b < -0.01], key=lambda x: x[1], reverse=True)
    creditors = sorted([(p, b) for p, b in balance.items() if b > 0.01], key=lambda x: x[1], reverse=True)

    transactions = []
    i, j = 0, 0
    while i < len(debtors) and j < len(creditors):
        debtor, debt = debtors[i]
        creditor, credit = creditors[j]
        pay = min(debt, credit)
        transactions.append({"from": debtor, "to": creditor, "amount": round(pay, 2)})
        debtors[i] = (debtor, debt - pay)
        creditors[j] = (creditor, credit - pay)
        if debtors[i][1] < 0.01:
            i += 1
        if creditors[j][1] < 0.01:
            j += 1

    return transactions, round(total, 2)