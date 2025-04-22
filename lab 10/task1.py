from tkinter import Menu
import psycopg2 
import csv 
conn = psycopg2.connect(
    dbname = "lab10" ,
    user = "postgres" , 
    password = "Superpasswordforsql", 
    host = "localhost",
    port = "5432"
)

cur = conn.cursor()
print("Connected") 
def inputs():
    global name , phone
    name = input("enter your name : ")
    phone =(input("enter your phone number: "))

def g_input():
    global need 
    need = input("Input the name or phonenumber you want need: ")


def Insert_from_console(name , phone):
    cur.execute("INSERT INTO phonebook (username , phonenumber) VALUES (%s , %s)" , (name , phone))
    conn.commit()
    
def read_from_csv():
    with open("constacs.csv" , 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO phonebook (username , phonenumber) VALUES (%s , %s)" , (row[0] , row[1]))

def Update():
    new_name = input("Новое имя вводи")
    new_phone = input("новый телефонный номер вводи ")
    old_name = input("Enter the name you want to remove: ")
    cur.execute(
        "UPDATE phonebook SET username = %s  ,  phonenumber = %s WHERE username = %s"  , (new_name , new_phone , old_name)
        )
    conn.commit()
    
def Del(thing):
    cur.execute("DELETE FROM phonebook WHERE username = %s OR phonenumber = %s" , (thing , thing))
    conn.commit()



def filtres():
    print("---------------------------------------------------------------")
    choose = int(input("CHOSE ONE (1 (All) , 2 (The only need (name))) , 3 (The only need (phonenumber))"))
    if choose == 1:
        cur.execute("SELECT * FROM phonebook")
    else:
        thing = g_input()
        if choose == 2:
            cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s" , (thing))
        elif choose == 3:
            cur.execute("SELECT * FROM phonebook WHERE phonenumber ILIKE %s" , (thing))
        else:
            print("try again(")
            filtres(thing)

    rows = cur.fetchall()
    for row in rows:
        print(row)



def menu():
    while True:
        print("ВЫБЕРИ ОДНУ ИЗ НИХ \n "  \
        "1. ДОбавить дату с консоли \n" \
        "2. ДОБАВИть дату с ксв файла \n" \
        "3. Обновить дату (нужно три инпута (старое имя новое имя новый телефон номер )) \n" \
        "4. удалить че нить (удаляет всю строкоу по дному из элементов имя или телефон номер )\n" \
        "5. фильтрует дату которая тебе нужна \n ")
        try:
            choice = int(input("ТВОЙ ЧОЙС : "))
        except ValueError:
            print("1 - 6 only!!")
            continue

        if choice == 1:
            inputs()
            Insert_from_console(name , phone)
        elif choice == 2:
            read_from_csv()
        elif choice == 3:
            
            Update()
        elif choice == 4:
            g_input()
            Del(need)
        elif choice == 5:
            filtres()
        elif choice == 6:
            print("quitting..")
            break
        else:
            print("Nuh-Uh")
        
menu()
cur.close()
conn.close()

