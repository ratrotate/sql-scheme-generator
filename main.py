import random
import argparse

# Library Constants
tables = ['Storage', 'Shop', 'Books', 'Clients']
columns = ['id', 'name', 'storeID', 'shopID', 'clientID', 'bookID', 'quantity']
names = ['storageName', 'shopName', 'booksName', 'clientsName']
storeName = ["производственный", "транзитно-перевалочный", "таможенный", "оптово-распределительный", "розничный", "резервный"]
shopName = ["Книжный бульвар", "Книголюб", "Книжная полка", "Новый книжный", "Книгоград"]
bookName = 	["Мастер и Маргарита", "Мёртвые души", "Двенадцать стульев", "Собачье сердце", "Война и мир", "Преступление и наказание", "Отверженные"]
clientName = ["Dark Carnage", "Fatal Destiny", "Ultimate Beast", "Masked Titan", "Frozen Gunner"]

# SQL QUERY Constants
create_table_3 = 'CREATE TABLE {}({} INT, {} VARCHAR(30), {} INT);'
insert_table_3 = 'INSERT INTO {}({}, {}, {}) VALUES ({}, "{}", {});'
create_table_4 = 'CREATE TABLE {}({} INT, {} VARCHAR(30), {} INT, {} INT);'
insert_table_4 = 'INSERT INTO {}({}, {}, {}, {}) VALUES ({}, "{}", {}, {});'

# Generator Params
counter, entropy = 10, 1  

def weightedRandom():
    return random.randint(0, round((counter - 1) * entropy))

def fillStorageTable():
    for line_num in range(0, counter):
        tmpStoreName = storeName[random.randint(0, len(storeName) - 1)]
        tmpShopId = weightedRandom()
        print(insert_table_3.format(tables[0], columns[0], names[0], columns[3], line_num, tmpStoreName, tmpShopId))   

def fillShopsTable():
    for line_num in range(0, counter):
        tmpShopName = shopName[random.randint(0, len(shopName) - 1)]
        tmpClientID = weightedRandom()
        tmpBookID = weightedRandom()
        print(insert_table_4.format(tables[1], columns[0], names[1], columns[4], columns[5], line_num, tmpShopName, tmpClientID, tmpBookID))

def fillBooksTable():
    for line_num in range(0, counter):
        tmpBookName = bookName[random.randint(0, len(bookName) - 1)]
        tmpQuantitiy = weightedRandom()
        print(insert_table_3.format(tables[2], columns[0], names[2], columns[6], line_num, tmpBookName, tmpQuantitiy))

def fillClientsTable():
    for line_num in range(0, counter):
        tmpClientName = clientName[random.randint(0, len(clientName) - 1)]
        tmpShopId = weightedRandom()
        print(insert_table_3.format(tables[3], columns[0], names[3], columns[3], line_num, tmpClientName, tmpShopId))   

def fillTable(table_name):
    if table_name == 'Storage':
        print(create_table_3.format(table_name, columns[0], names[0], columns[3]))
        fillStorageTable()

    if table_name == 'Shop':
        print(create_table_4.format(table_name, columns[0], names[1], columns[4], columns[5]))
        fillShopsTable()
 
    if table_name == 'Books':
        print(create_table_3.format(table_name, columns[0], names[2], columns[6]))
        fillBooksTable()

    if table_name == 'Clients':
        print(create_table_3.format(table_name, columns[0], names[3], columns[3]))
        fillClientsTable()
    
def getGeneratorSetup():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--c', metavar='counter', type=int, help='number of rows in the table, default = 10')
    parser.add_argument('--e', metavar='entropy', type=float, help='entropy of ids to be generated, default = 1')
    args = parser.parse_args()
    if args.c is not None: 
        counter = args.c
    if args.e is not None:
        entropy = args.e
    return counter, entropy
 
if __name__ == "__main__":
    counter, entropy = getGeneratorSetup()
    for table in tables:
        fillTable(table)
