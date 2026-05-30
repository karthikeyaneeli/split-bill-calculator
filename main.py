from calculator import calculate_splits

def get_people():
    print("\nEnter names of people (comma-separated):")
    raw = input("> ").strip()
    return [p.strip() for p in raw.split(",") if p.strip()]

def get_expenses(people):
    expenses = []
    print("\nAdd expenses (press Enter with empty description to finish):")
    while True:
        print(f"\n  Description: ", end="")
        desc = input().strip()
        if not desc:
            break
        try:
            amount = float(input("  Amount (₹): ").strip())
        except ValueError:
            print("  Invalid amount. Try again.")
            continue
        print(f"  Paid by (options: {', '.join(people)}): ", end="")
        paid_by = input().strip()
        if paid_by not in people:
            print(f"  '{paid_by}' not in the group. Skipping.")
            continue
        expenses.append({"desc": desc, "amount": amount, "paid_by": paid_by})
    return expenses

def show_summary(people, expenses, transactions, total):
    print("\n" + "="*40)
    print(f"Total: ₹{total:.0f}  |  Per person: ₹{total/len(people):.0f}")
    print("\nExpenses:")
    for e in expenses:
        print(f"  {e['desc']:<20} ₹{e['amount']:<8.0f} paid by {e['paid_by']}")
    print("\nSettlements:")
    if not transactions:
        print("  Everyone is settled up!")
    else:
        for t in transactions:
            print(f"  {t['from']} → {t['to']}: ₹{t['amount']:.0f}")
    print("="*40)

def main():
    print("╔══════════════════════════════╗")
    print("║    Split Bill Calculator     ║")
    print("╚══════════════════════════════╝")
    people = get_people()
    if len(people) < 2:
        print("Need at least 2 people.")
        return
    expenses = get_expenses(people)
    if not expenses:
        print("No expenses added.")
        return
    transactions, total = calculate_splits(people, expenses)
    show_summary(people, expenses, transactions, total)

if __name__ == "__main__":
    main()