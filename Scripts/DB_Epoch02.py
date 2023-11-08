FILE_NAME = 'Scripts/src/database.txt'

def read_record_by_id(record_id):
    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()
        for line in lines:
            id, name, age = line.strip().split(',')
            if id == record_id:
                return (id, name, age)
    return None

def add_record(id, name, age):
    with open(FILE_NAME, 'a') as file:
        file.write(f"{id},{name},{age}\n")

def delete_record(record_id):
    records = read_all_records()
    with open(FILE_NAME, 'w') as file:
        for record in records:
            if record[0] != record_id:
                file.write(','.join(record) + '\n')

def update_record(record_id, name, age):
    records = read_all_records()
    with open(FILE_NAME, 'w') as file:
        for record in records:
            if record[0] == record_id:
                file.write(f"{record_id},{name},{age}\n")
            else:
                file.write(','.join(record) + '\n')

def read_all_records():
    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()
    return [tuple(line.strip().split(',')) for line in lines]

def main():
    while True:
        print("\n-----------------------")
        print("TXT Database Menu:")
        print("1. Read a record by ID")
        print("2. List all records")
        print("3. Add record")
        print("4. Delete record")
        print("5. Update record")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            id = input("Enter ID to read: ")
            record = read_record_by_id(id)
            if record:
                print(record)
            else:
                print(f"No record found for ID: {id}")
        elif choice == "2":
            records = read_all_records()
            for record in records:
                print(record)
        elif choice == "3":
            id = input("Enter ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            add_record(id, name, age)
        elif choice == "4":
            id = input("Enter ID to delete: ")
            delete_record(id)
        elif choice == "5":
            id = input("Enter ID to update: ")
            name = input("Enter new Name: ")
            age = input("Enter new Age: ")
            update_record(id, name, age)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
