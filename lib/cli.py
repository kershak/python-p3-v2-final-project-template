# lib/cli.py

#import inquirer
from inquirer.themes import GreenPassion
import pyfiglet
from helpers import (
    exit_program,
    list_rmas,
    find_rma_by_id,
    #find_rma,
    create_rma,
    update_rma,
    delete_rma,
    list_products,
    find_prodcut_by_name,
    find_product_by_id,
    create_product,
    update_product,
    delete_product
)


def main():
    print(pyfiglet.figlet_format("Welcome to RMA tracking system!"))
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_rmas()
        elif choice == "2":
            find_rma()
        elif choice == "3":
            rma_settings()
            choice = input(">>")
            if choice == "0":
                main()
            elif choice == "1":
                create_rma()
            elif choice == "2":
                update_rma()
            elif choice == "3":
                delete_rma()
            elif choice == "4":
                find_rma_by_id()
            else:
                print("Invalid choice")
        elif choice == "4":
            list_products()
        elif choice == "5":
            find_prodcut_by_name()
        elif choice == "6":
            product_settings()
            choice = input(">>")
            if choice == "0":
                main()
            elif choice == "1":
                create_product()
            elif choice == "2":
                update_product()
            elif choice == "3":
                delete_product()
            elif choice == "4":
                find_product_by_id()
            else:
                print("Invalid choice")
        else:
           print("Invalid choice")


def menu():
#     questions = [
#         inquirer.List('option', 
#                       message = "Please select an option: ",
#                       choices = [
#                           "0. Exit the program",
#                           "1. List RMAs",
#                           "2. Find RMA",
#                           "3. RMA settings:",
#                           "4. List products",
#                           "5. Find products by name",
#                           "6. Products settings:"
#                       ],),
#     ]
#     answers = inquirer.prompt(questions, theme=GreenPassion())
    
#     return str(answers ['option'] [0])

# def rma_settings():
#     questions = [
#         inquirer.List('rma_option', 
#                       message= "Here you can create , update or delete an RMA",
#                       choices= [
#                           "0. Back to main menu:",
#                           "1. Create RMA",
#                           "2. Update RMA",
#                           "3. Delete RMA"
#                       ],),
#     ]
#     inquirer.prompt(questions, theme= GreenPassion())
#     #return str(answers ['rma_option'][0])

# def product_settings():
#     questions = [
#         inquirer.List('product_option',
#                       message= "Here you can create, update or delete products",
#                       choices= [
#                           "0. Back to main menu:",
#                           "1. Create Product",
#                           "2. Update Product",
#                           "3. Delete Product"
#                       ],),
#     ]
#     inquirer.prompt(questions, theme= GreenPassion())
#     #return str(answers['product_option'][0])

    print("Please select an option:")
    print("0. Exit the program")
    print("1. List RMAs")
    print("2. Find RMA")
    print("3. RMA settings")
    print("4. List products")
    print("5. Find products by name")
    print("6. Product settings")

def rma_settings():
    print("0. Back to main menu:")
    print("1. Create RMA")
    print("2. Update RMA")
    print("3. Delete RMA")
    print("4. Find RMA by id")

def product_settings():
    print("0. Back to main menu: ")
    print("1. Create Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Find Products by id")


if __name__ == "__main__":
    main()
