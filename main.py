# main.py
from database import initialize_system
from display import show_all_inventory
from logic import make_sale, get_low_stock_report 

def main():
    initialize_system()
    
    while True:
        print("\n--- 🛒 LCU SUPERMARKET ---")
        print("1. View Full Inventory")
        print("2. Record a Sale")
        print("3. VIEW LOW STOCK ALERTS")
        print("4. Sales Report")
        print("5. Exit")
        
        choice = input("\nSelect: ")
        
        if choice == '1':
            show_all_inventory()
            
        elif choice == '2':
            make_sale()
            
        elif choice == '3': 
            alerts = get_low_stock_report()
            print("\n⚠️  LOW STOCK WARNING ⚠️")
            if not alerts:
                print("All items are well stocked.")
            else:
                print(f"{'ID':<6} {'Product Name':<35} {'Qty Left'}")
                for item in alerts:
                    print(f"{item[0]:<6} {item[1]:<35} {item[2]} (Min: {item[3]})")
                    
        elif choice == '4':
            pass
            
        elif choice == '5':
            break

if __name__ == "__main__":
    main()