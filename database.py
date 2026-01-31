import sqlite3
import random

def initialize_system():
    conn = sqlite3.connect('supermarket.db')
    cursor = conn.cursor()

    # 1. Create Tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY, name TEXT, category TEXT, 
        price INTEGER, quantity INTEGER, min_stock INTEGER)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT, qty_sold INTEGER, total_val INTEGER, 
        sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')


    cursor.execute("SELECT COUNT(*) FROM inventory")
    if cursor.fetchone()[0] == 0:
        print("Creating Database with Branded Items...")
        
        #CATEGORY LISTS
        groceries = ["Rice", "Semovita", "Semolina", "Spaghetti", "Spaghettini", "Dangote Sugar", "Mr Chef Salt", "Soya Oil", "Beans", "Golden Morn", "Milo", "Dano"]
        g_sizes = ["250g", "500g", "1kg", "5kg", "10kg"]

        beverages = ["Coke", "Pepsi", "Eva Water", "Hollandia Youghurt", "Malta Guiness", "Amstel Malt", "Dudu", "Eva Wine"]
        b_sizes = ["60cl", "100cl", "1L", "2L", "5L"]

        t_items = ["Soap", "Toothpaste", "Brush", "Tissue", "Shampoo", "Lotion", "Deodorant", "Pad", "Gel", "Cream"]
        t_brands = ["Dettol", "Oral-B", "Pepsodent", "Beloxxi", "Lux", "Nivea", "Always", "Gillette", "Vaseline"]

        h_items = ["Detergent", "Bleach", "Sponge", "Broom", "Mop", "Insecticide", "Bulb", "Battery", "Match", "Cleaner"]
        h_brands = ["Ariel", "Hypo", "Omo", "Sunshine", "Raid", "Panasonic", "Tiger", "Jif", "So Klin"]

        s_items = ["Biscuit", "Chips", "Chocolate", "Sweets", "Bread", "Cake", "Peanuts", "Popcorn", "Gum", "Cookies"]
        s_brands = ["Yale", "Oxford", "McVities", "Pringles", "Cadbury", "Nestle", "Butterfield", "Nasco"]

        all_items = []

        # 3. Generate 50 items for each of the 5 categories (250 Total)
        for i in range(50):
            # Groceries
            g_name = f"{groceries[i % len(groceries)]} ({g_sizes[i % len(g_sizes)]})"
            all_items.append((100+i, g_name, "Grocery", random.randint(2000, 15000), random.randint(10, 50), 10))
            
            # Beverages
            b_name = f"{beverages[i % len(beverages)]} ({b_sizes[i % len(b_sizes)]})"
            all_items.append((200+i, b_name, "Beverages", random.randint(500, 8000), random.randint(10, 50), 10))

            # Toiletries
            t_name = f"{t_items[i % len(t_items)]} ({random.choice(t_brands)})"
            all_items.append((300+i, t_name, "Toiletries", random.randint(500, 6000), random.randint(5, 50), 10))
            
            # Household
            h_name = f"{h_items[i % len(h_items)]} ({random.choice(h_brands)})"
            all_items.append((400+i, h_name, "Household", random.randint(1000, 10000), random.randint(5, 50), 10))
            
            # Snacks
            s_name = f"{s_items[i % len(s_items)]} ({random.choice(s_brands)})"
            all_items.append((500+i, s_name, "Snacks", random.randint(200, 5000), random.randint(5, 50), 10))

        cursor.executemany("INSERT INTO inventory VALUES (?, ?, ?, ?, ?, ?)", all_items)
        conn.commit()
        print("✓ Database Initialized: 250 branded items ready.")
    
    conn.close()

if __name__ == "__main__":
    initialize_system()