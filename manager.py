import sqlite3

class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

#Analisar como os produtos estao sendo salvos com esta funcao   
def save_data(name, price, quantity):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS products (name text, price text, quantity text)")
    cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", (name, price, (quantity)))

    conn.commit()
    conn.close()
    
def create_product():
    name = str(input("Titulo\n"))
    price = float(input("Preco\n"))
    quantity = int(input("Quantidade\n"))

    save_data(name, price, quantity)

def remove_product(removed_name):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products WHERE name = ?", (removed_name,))
    if cursor.rowcount > 0:
        conn.commit()
        conn.close()
        return True  # Produto excluído com sucesso
    else:
        conn.close()
        return False  # Produto não encontrado

def edit_name(name):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    old_name = cursor.execute("SELECT name FROM products WHERE name = ?", (name,)).fetchone()[0]

    new_name = str(input("Novo Titulo\n"))

    if not new_name:
        raise ValueError("Um novo nome deve ser definido!")

    cursor.execute("UPDATE products set name = ? WHERE name = ?",
                   (new_name, old_name))
    
    conn.commit()
    conn.close()

def edit_price(name):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    old_name = cursor.execute("SELECT name FROM products WHERE name = ?", (name,)).fetchone()[0]

    new_price = float(input("Novo Preco\n"))

    if not new_price:
        raise ValueError("Um novo valor (positivo) deve ser definido!")

    cursor.execute("UPDATE products set price = ? WHERE name = ?",
                   (new_price, old_name))
    
    conn.commit()
    conn.close()

def edit_quantity(name):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    old_name = cursor.execute("SELECT name FROM products WHERE name = ?", (name,)).fetchone()[0]

    new_quantity = int(input("Nova Quantidade\n"))

    if not new_quantity:
        raise ValueError("Um nova quantidade (positiva) deve ser definido!")

    cursor.execute("UPDATE products set quantity = ? WHERE name = ?",
                   (new_quantity, old_name))
    
    conn.commit()
    conn.close()
    
def sell_product(name):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    old_name = cursor.execute("SELECT name FROM products WHERE name = ?", (name,)).fetchone()[0]
    cursor.execute("UPDATE producs set quantity = quantity - 1 WHERE name = ?",
                   (name))
    
    conn.commit()
    conn.close()
    
def show_product():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    print(" Produtos:")
    for product in products:
        print(" ", product)

    conn.close()

while True:
    print('Seja Bem-Vindo ao Gestor de Estoque!')
    print(show_product())
    print("1 - Editar Nome    2 - Editar Preco    3 - Editar Quantidade    4 - Criar Produto    5 - Remover Produto")
    operacao1 = int(input("Operacao escolhida:"))
    if operacao1 == 1:
        edited_name = str(input("Insira o nome do produto que deseja alterar:"))
        edit_name(edited_name)
        print("Nome alterado!")

    if operacao1 == 2:
        edited_price = str(input("Insira o nome do produto que deseja alterar:"))
        edit_price(edited_price)
        print("Preco alterado!")
      

    if operacao1 == 3: 
        edited_quantity = str(input("Insira o nome do produto que deseja alterar:"))
        edit_quantity(edited_quantity)
        print("Quantidade alterada!")

    if operacao1 == 4:
        create_product()
        print("Produto Adicionado!")

    if operacao1 == 5:
        removed_product = str(input("Insira o nome do produto que deseja remover:"))
        remove_product(removed_product)
        print('Produto Removido!')

    continuar = input("Voltar? (s/n): ")
    if continuar.lower() != 's':
        break

 

        