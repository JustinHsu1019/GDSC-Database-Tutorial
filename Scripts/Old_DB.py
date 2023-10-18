DATA = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 35},
    {"id": 4, "name": "David", "age": 28},
    {"id": 5, "name": "Eva", "age": 32}
]

def select_record_by_id(record_id):
    """根據ID選擇資料"""
    for record in DATA:
        if record["id"] == record_id:
            return record
    return None

def main():
    while True:
        print("\n-----------------------")
        print("Simple Database Menu:")
        print("1. Select record by ID")
        print("2. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            record_id = int(input("Enter record ID: "))
            record = select_record_by_id(record_id)
            if record:
                print(record)
            else:
                print(f"No record found for ID: {record_id}")
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
