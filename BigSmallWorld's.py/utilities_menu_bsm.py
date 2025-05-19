from products_functions import load_product, search_product, delete_product

def menu_products_bsm(user_id):

    while True:
        answer = int(input(
        """ 
        =============================
        Welcome to menu of products, choose an option \n
        1. Load Products
        2. Search Products
        3. Delete Products
        3. Exit 
        =============================\n
        Option: """))

        match answer:
            case 1:
                load_product(user_id)
            case 2:
                search_product()
            case 3:
                delete_product()
            case 4:
                from main import main
                main()