goods = []
sells = []
archive = []

while True:
    archive.extend(goods)
    print("Welcome to our Store!\n What do you want to do? \n 1. Add a good \n 2. View goods \n 3. Sell goods \n 4. Replace all goods \n 5. Print Sell list \n 6. History of goods \n 7. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        good = input("Write a name of good ==> ")
        goods.append(good)
        print('\n Success \n')
    elif choice == '2':
        for i in goods:
            print(f"Your goods: {i}")
    elif choice == '3':
        for i in goods:
            print(f"Your goods: {i}")
        sellgood = input('What do you want to sell? ')
        goods.remove(sellgood)
        sells.append(sellgood)
        print("\n You have already sold it! \n")
    elif choice == "4":
        replacegoods = input("Write a new goods: ")
        replacegoods = list()
        goods.clear()
        goods.append(replacegoods)
        print('\n Success \n')
    elif choice == "5":
        for s in sells:
            print(f'Your sell list: {s}')
    elif choice == "6":
        for a in archive:
            print(f"Your archive: {a}")
    elif choice =="7":
        print("\n It is stopping \n")
        break
        

        
        

        
        
        

