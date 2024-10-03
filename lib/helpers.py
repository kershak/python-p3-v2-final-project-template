# lib/helpers.py
from models.rma import Rma
from models.product import Product
from tabulate import tabulate

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_rmas():
    rmas = Rma.get_all()
    for rma in rmas:
        print(rma)

def find_rma_by_id():
    rma_id = input("Enter RMA id to find: ")
    rma = Rma.find_by_id(int(rma_id))
    if rma:
        print(rma)
    else: 
        print("RMA not found")
        
# def find_rma():
#     rma_number = input("Enter RMA number to find: ")
#     rmas = Rma.find_by_number(rma_number)
#     if rmas:
#         for rma in rmas:
#             print(rma)
#     else:
#         print("RMA not found.")

def create_rma():
    rma_number = input("Enter the RMA number: ").upper
    received_on = input("Enter date received: ")
    products = input("Enter products on this RMA: ").upper
    try:
        new_rma = Rma.create(rma_number, received_on, products)
        print(f"Sucess: {new_rma}")
    except Exception as exc:
        print("Error creating RMA: ", exc)

def update_rma():
    id = input("Enter the RMA id:")
    if rma_update := Rma.find_by_id(id):
        try:
            rma = input("Enter updated rma number: ")
            Rma.rma_number = str(rma).upper
            received_on = input("Enter revised date: ")
            Rma.received_on = str(received_on)
            products= input("Enter updated list of products: ")
            Rma.products = str(products).upper
            Rma.update(id, rma, received_on)
            print(f'Success updating: {rma_update}')
        except Exception as exc:
            print("Error updating RMA", exc)
    else:
        print(f'Product {id} not found')


def delete_rma():
    id = input ("Enter the RMA id to be deleted: ")
    try:
        id = int(id)
        rma = Rma.find_by_id(id)

        if rma:
            Rma.delete(id)
            print(f'RMA entry {id} has been deleted')
        else:
            print(f'RMA {id} not found')
    except ValueError:
        print("Invalid input")
    except Exception as exc:
        print("Error deleting RMA", exc)

def list_products():
    products = Product.get_all()
    for product in products:
        print(product)

def find_product_by_id():
    product_id = input("Enter Product id to find: ")
    product = Product.find_by_id(int(product_id))
    if product:
        print(product)
    else:
        print("Product not found.")

def find_prodcut_by_name():
    model = input("Enter the product name.")
    product = Product.find_by_model(model)
    if product:
        print(product)
    else:
        print(f"Product model {model} not found.")

def create_product():
    model = input("Enter mode number: ")
    price = float(input("Enter price: "))
    description = input("Enter description: ")
    try:
        new_product = Product.create(model, price, description)
        print(f"Success: {new_product}")
    except Exception as exc:
        print("Error creating product: ", exc)

def update_product():
    id = input("Enter the product id: ")
    if product_update := Product.find_by_id(id):
        try:
            model = input("Enter updated model number: ")
            Product.model = str(model)
            price = input("Enter updated price for product: ")
            Product.price = float(price)
            description = input("Enter revised description for product: ")
            Product.description = str(description)
            Product.update(id, model, price, description)
            print(f'Success updating: {product_update}')
        except Exception as exc:
            print("Error updating Product", exc)
    else:
        print(f'Product {id} not found')

def delete_product():
    id = input("Enter the Product id to be deleted: ")
    try: 
        id = int(id)
        rma = Product.find_by_id(id)
        
        if rma:
            Product.delete(id)
            print(f'Product {id} has been deleted')
        else:
            print(f'Product {id} not found')
    except ValueError:
        print("Invalid input.")
    except Exception as exc:
        print("Error deleting product", exc)