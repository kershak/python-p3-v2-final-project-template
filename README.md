# Phase 3 CLI+ORM Project

# Returns tracking system:

## Description:

This project at this stage is only the begining of a much bigger project that I have plan.
I have build this help me at my current job, where I wear multiple hats (IT and technical support), I will be using this for my technical support roll where I receive, evalute , repair and return products that are not working properly.

## Features:

RMATS (RMA tracking system) helps track the returns, when it was received , when it was ship back.
It stores in tables the items or products the company manufactures, and the rma information such as : rma 
number, date received , items inside the rma.

## File structure:

Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    |   |── product.py
    │   └── rma.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

## Installation:

1. **Clone the template repository:**
    - Git clone ( git@github.com:kershak/python-p3-v2-final-project-template.git )
    - cd (enter repo folder)

2. **Install Dependencies:**
    - Python3
    - pipenv install
    - pipenv shell
    - Inquirer (selecting the options with arrows)
    - Pyfiglet (used on my header)

3. **How to run code:**
    - python lib/cli.py

## Menus:

- Main menu:
    - 0. Exit the program
    - 1. List RMAs
    - 2. Find RMA
    - 3. RMA settings
    - 4. List products
    - 5. Find products by name
    - 6. Products settings

- Sub menu:
    - If select RMA settings:
        - 0. Back to main menu
        - 1. Create RMA
        - 2. Update RMA
        - 3. Delete RMA
        - 4. Find RMA by id

    - If select Products settings
        - 0. Back to main menu
        - 1. Create Product
        - 2. Update Product
        - 3. Delete Product
        - 4. Find Product by id

## Example

\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   |  _ \|  \/  |  / \
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | |_) | |\/| | / _ \
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | |  _ <| |  | |/ ___ \
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_| \_\_|  |_/_/   \_\

 _                  _    _                             _                 _
| |_ _ __ __ _  ___| | _(_)_ __   __ _   ___ _   _ ___| |_ ___ _ __ ___ | |
| __| '__/ _` |/ __| |/ / | '_ \ / _` | / __| | | / __| __/ _ \ '_ ` _ \| |
| |_| | | (_| | (__|   <| | | | | (_| | \__ \ |_| \__ \ ||  __/ | | | | |_|
 \__|_|  \__,_|\___|_|\_\_|_| |_|\__, | |___/\__, |___/\__\___|_| |_| |_(_)
                                 |___/       |___/

Please select an option:
0. Exit the program
1. List RMAs - generates a list of all RMAs in the database.
2. Find RMA - finds an RMA by inputing the RMA number.
3. RMA settings - Enter a sub menu for more RMA specific options.
4. List products - generates a list of all products in the database.
5. Find products by name - finds a product by inputing the product name.
6. Product settings - Enter a sub menu for more product specific options.
> 3
0. Back to main menu: - returns to the main menu.
1. Create RMA - creates a new RMA instances.
2. Update RMA - updates an instances on the RMA database.
3. Delete RMA - delete an instance on the RMA database.
4. Find RMA by id - finds an RMA by inputing an ID number.
>>

Please select an option:
0. Exit the program
1. List RMAs 
2. Find RMA
3. RMA settings
4. List products
5. Find products by name
6. Product settings
> 6
0. Back to main menu: - returns to the main menu.
1. Create Product - creates a new Product instances.
2. Update Product - updates an instance on the Product database.
3. Delete Product - deletes an instance on the Product database.
4. Find Products by id - finds an instance by inputing an ID number.
>>

## Conclusion:

After working on this project I realized I can make it so much bigger and interactive in the future.

Copyrights - Nills Lopez