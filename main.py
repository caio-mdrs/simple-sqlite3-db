import sqlite3

banco = sqlite3.connect('database.db')

cursor = banco.cursor()

def create_Db():
    cursor.execute('CREATE TABLE main (ID int, Nome text, Idade int, Email text)')

    banco.commit()

def insert_Data():
    #last_id = cursor.execute('SELECT LAST_VALUE(ID) FROM main')
    #print(f"ID: {last_id}")
    command = input("ID|'Nome'|Idade|'Email':")
    cursor.execute(f"INSERT INTO main VALUES({command})")
    print(f"{'='*20}\nDados: {command}\nInseridos com sucesso\n{'='*20}")
    banco.commit()

def insert_Command():
    command = input('Digite o comando: ')
    cursor.execute(command)
    print(f"{'='*20}\nComando {command} executado\n{'='*20}")
    banco.commit()

def print_Data():
    cursor.execute('SELECT * FROM main')
    print(f"{'='*20}\n{cursor.fetchall()}\n{'='*20}")

while True:
    choice = int(input("1: Criar banco\n2: Inserir dados\n3: Executar comando\n4: Visualizar dados\nEscolha uma opção:"))
    if choice == 1:
        create_Db()
    elif choice == 2:
        insert_Data()
    elif choice == 3:
        insert_Command()
    elif choice == 4:
        print_Data()
    else:
        print(F"{'='*20}\nOpção inválida\n{'='*20}")
