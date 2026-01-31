import sqlite3

def show_all_inventory():
    conn = sqlite3.connect('supermarket.db')
    cursor = conn.cursor()
    
    # Fetch all 250 branded items
    cursor.execute("SELECT id, name, category, price, quantity, min_stock FROM inventory ORDER BY id ASC")
    rows = cursor.fetchall()

    print("\n" + "="*100)
    print(f"{'ID':<6} {'Product Name':<35} {'Category':<15} {'Price':<12} {'Stock':<8} {'Status'}")
    print("-" * 100)

    for row in rows:
        # ₦ Currency and Comma formatting
        formatted_price = f"₦{row[3]:,}"
        
        # Low Stock Alert Logic
        status = "!!! LOW !!!" if row[4] <= row[5] else "OK"
        
        print(f"{row[0]:<6} {row[1]:<35} {row[2]:<15} {formatted_price:<12} {row[4]:<8} {status}")
    
    print("="*100 + "\n")
    conn.close()