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
    return name , phone

def g_input():
    global need 
    need = input("Input the name or phonenumber you want need: ")
    return need


def Insert_from_console(name , phone): #1
    cur.execute("INSERT INTO phonebook (username , phonenumber) VALUES (%s , %s)" , (name , phone))
    conn.commit()
    
def read_from_csv(): #2 
    with open("constacs.csv" , 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO phonebook (username , phonenumber) VALUES (%s , %s)" , (row[0] , row[1]))

def Update(): #3
    new_name = input("Новое имя вводи > ")
    new_phone = input("новый телефонный номер вводи > ")
    old_name = input("Enter the name you want to remove: ")
    cur.execute(
        "UPDATE phonebook SET username = %s  ,  phonenumber = %s WHERE username = %s"  , (new_name , new_phone , old_name)
        )
    conn.commit()
    
def Del(thing): #4
    cur.execute("DELETE FROM phonebook WHERE username = %s OR phonenumber = %s" , (thing , thing))
    conn.commit()



def filtres(): #5
    print("---------------------------------------------------------------")
    try:
        choose = int(input("CHOSE ONE (1 (All) , 2 (The only need (name))) , 3 (The only need (phonenumber))"))
        if choose == 1:
            cur.execute("SELECT * FROM phonebook")
        else:
            thing = input()
            if choose == 2:
                cur.execute("SELECT * FROM phonebook WHERE username ILIKE %s" , (thing))
            elif choose == 3:
                cur.execute("SELECT * FROM phonebook WHERE phonenumber ILIKE %s" , (thing))
            else:
                print("try again(")
                filtres()
            rows = cur.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Ошибка {e}")
   
    

def search_by_shablon(): #6
    search = input("Введите шаблон для поиска > ")
    try:
        cur.execute(
            "SELECT * FROM phonebook WHERE username ILIKE %s OR phonenumber ILIKE %s OR username ILIKE %s",
            (f"{search}%", f"%{search}", f"%{search}%")
        )
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Ошибка при поиске:", e)


def using_procedure(): #7
    inputs()
    cur.execute("CALL insert_or_update_user(%s, %s);", (name , phone))

def enter_list(): #8
    size = int(input("ENTER HOW MANY YOU WOULD LIKE TO ENTER > "))
    names =[]
    numbers = []
    for i in range (size):
        name = input("ENTER THE NAME > ")
        phonenumber = input("ENTER THE PHONE NUMBER > ")

        names.append(name) 
        numbers.append(phonenumber) 

    cur.execute("CALL add_new_users (%s , %s)" , (names , numbers))
    conn.commit()
   
def insert_users(): #9
    size = int(input("ENTER the number of users you want to insert > "))

    names = []
    nums = []

    for i in range(size):
        name = input(f"ENTER THE NAME of user  {i+1} > ")
        phonenum = input(f"Enter the phone number of user {i+1} > ")

        names.append(name)
        nums.append(phonenum)

    try:
        for i in range(size):
            cur.execute("CALL insert_new_users(%s , %s )" , (names[i] , nums[i]))
        conn.commit()
        print("сработало")
    except Exception as e:
        print(f"ошибка {e}")
    
def get_users_page(): #10
    page_limit = int(input("СКОЛЬКИХ ХОТИТЕ УВИДЕТЬ? > "))
    page_offset = int(input("СКОЛЬКИХ ХОТИТЕ СКИПНУТЬ  > "))
    try:
        cur.execute("SELECT * FROM public.get_users_with_pagination(%s , %s)" , (page_limit , page_offset ))
        rows = cur.fetchall()

        for row in rows:
            print(f"ID {row[0]} , USERNAME > {row[1]} , PHONENUMBER > {row[2]}") 
    except Exception as e:
        conn.rollback() #откат всех измении в дб которые прошли текущие транзакции (оно спасло меня от постоянной ошибккииии!!! )
        print(f"oshibka {e}")
    

def delete_user(): #11
    
    g_input()
    try:
        cur.execute("CALL delete_users (%s)" , (need , ))
        conn.commit()
        print("udalil")
    except Exception as e:
        print("ОШИБОЧКА" , e)

    

   

def menu():
    while True:
        print("ВЫБЕРИ ОДНУ ИЗ НИХ \n "  \
        "1. ДОбавить дату с консоли \n" \
        "2. ДОБАВИть дату с ксв файла \n" \
        "3. Обновить дату (нужно три инпута (старое имя новое имя новый телефон номер )) \n" \
        "4. удалить че нить (удаляет всю строкоу по дному из элементов имя или телефон номер )\n" \
        "5. фильтрует дату которая тебе нужна \n " \
        "6. искать по части слова\n"  \
        "7.Добавить или обновить юзеров \n" \
        "8. Добавить сразу нескольких в дб \n" \
        "9.  Добавление юзеров с правильным номером телефона (11 цифр)\n" \
        "10. Получить количество нужных юзеров  \n" \
        "11.  Удаление юзеров по имени или телефону \n" \
        "12.  Выйти \n" \
         
        )
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
            search_by_shablon()
        elif choice == 7:
            using_procedure()
        elif choice == 8:
            enter_list()
        elif choice == 9:
            insert_users()
        elif choice == 10:
            get_users_page()
        elif choice == 11:
            delete_user()
        elif choice == 12:
            print("quitting..")
            break
        else:
            print("Nuh-Uh")
        
menu()
cur.close()
conn.close()

