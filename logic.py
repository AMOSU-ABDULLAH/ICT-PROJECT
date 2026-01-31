import sqlite3

def make_sale():
    conn = sqlite3.connect('supermarket.db')
    cursor = conn.cursor()
    
    try:
        p_id = int(input("\nEnter Product ID: "))
        qty = int(input("Enter Quantity to buy: "))
        
        cursor.execute("SELECT name, price, quantity FROM inventory WHERE id = ?", (p_id,))
        item = cursor.fetchone()
        
        if item and item[2] >= qty:
            total = item[1] * qty
            # Update stock
            cursor.execute("UPDATE inventory SET quantity = quantity - ? WHERE id = ?", (qty, p_id))
            # Save to sales report
            cursor.execute("INSERT INTO sales (item_name, qty_sold, total_val) VALUES (?, ?, ?)", 
                           (item[0], qty, total))
            conn.commit()
            print(f"✓ Success: Sold {qty} {item[0]} for ₦{total:,}")
        else:
            print("❌ Error: ID not found or Out of Stock!")
    except ValueError:
        print("❌ Error: Please enter numbers only.")
    
    conn.close()

def get_low_stock_report():
    conn = sqlite3.connect('supermarket.db')
    cursor = conn.cursor()
    
    #Filter for quantity <= min_stock (10)
    cursor.execute("SELECT id, name, quantity, min_stock FROM inventory WHERE quantity <= min_stock")
    low_items = cursor.fetchall()
    conn.close()
    return low_items