def menu():
    
    global choice
    print('===========================================')
    print('       = Inventory Management Menu =       ')
    print('===========================================')
    print('(1) Add New Item to Inventory')
    print('(2) Remove Item from Inventory')
    print('(3) Update Inventory')
    print('(4) Search Item in Inventory')
    print('(5) Print Inventory Report')
    print('(6) Quit')
    
    choice = int(input("Enter choice: "))
    print()
    
def add_item():

    global list
    print('===========================================')
    print('           = Select Item Menu =            ')
    print('===========================================')
    print('(1) Add fruit')
    print('(2) Add vegetables')
    print('(3) Add grain')
    
    
    list = [[],[],[]]
    choice = int(input("Enter choice: "))
    item = input("Enter item (e.g. Apples): ")
    cost_price = int(input("Enter cost price: "))
    sales_price = int(input("Enter sales price: "))
    stock = int(input("Enter stock: "))
    print()
         
    dict = {"Item":item, "Cost":cost_price, "Sales":sales_price, "Stock":stock}
    list[choice - 1].append(dict)
    
def remove_item():
    
    print("Geef het item op dat u wilt verwijderen.")
    z = int(input("Geef stellingnummer op (e.g. 1 = Fruit, 2 = Vegetables, 3 = Grain): "))
    y = int(input("Geef rijnummer op (e.g. vanaf 1): "))
    del list[z - 1][y - 1]
   
def update_item():
    
    z = int(input("Geef stellingnummer op (e.g. 1 = Fruit, 2 = Vegetables, 3 = Grain): "))
    y = int(input("Geef rijnummer op (e.g. vanaf 1): "))
    key = input("Geef de key op dat uw wilt updaten (e.g. Item, Cost): ")
    update = int(input("Update " + key + " value : "))
    list[z - 1][y - 1][key] = update
    
def search_item():
   
    item = input("Geef een item op (e.g. Appels): ")
    print()
    for z in range(len(list)):
        for y in range(len(list[z])):
            for key in list[z][y]:
                if list[z][y][key] == item:
                    print('===========================================')
                    for key in list[z][y]:
                        print(format(key, "<10"), format(list[z][y][key], "<10"))
                    break
    print('===========================================')
    print()

def print_items():
   
    print('===========================================')
    print(format("Item", "<10"), format("Cost", "<10"),  format("Sales", "<10"),   format("Stock", "<10"))
    print('===========================================')
    for z in range(3):
        for y in range(len(list[z])):
            for key in list[z][y]:
                print(format(list[z][y][key], "<10"), end=" ")
            print()
        print()

def main():
    
    while True: 
        menu()
        if choice == 1:
            add_item()
        elif choice == 2:
            remove_item()
        elif choice == 3:
            update_item()
        elif choice == 4:
            search_item()
        elif choice == 5:
            print_items()
        else:
            exit()

main()