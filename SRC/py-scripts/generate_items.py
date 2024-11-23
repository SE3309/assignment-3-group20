from faker import Faker
import mysql.connector
import random
from datetime import date

# Ensure unique item IDs
used_ids = set()

# Function to generate unique item IDs
def generate_unique_item_id():
    while True:
        item_id = random.randint(1000, 9999)  # Item IDs are within the range 1000 to 9999
        if item_id not in used_ids:
            used_ids.add(item_id)
            return item_id

# Function to generate equipment data
def generate_equipment_data(fake):
    item_id = generate_unique_item_id()
    category = fake.random_element(elements=('Beverage', 'Dairy', 'Carbohydrate', 'Protein', 'Produce', 'Condiment'))

    # Item name based on category
    if category == 'Beverage':
        item_name = fake.random_element(elements=('Water bottle', 'Juice box', 'Pop can', 'Coffee', 'Tea'))
    elif category == 'Dairy':
        item_name = fake.random_element(elements=('Milk', 'Cheese', 'Yogurt', 'Sour cream', 'Butter'))
    elif category == 'Carbohydrate':
        item_name = fake.random_element(elements=('Bread', 'Muffin', 'Croissant', 'Pasta'))
    elif category == 'Protein':
        item_name = fake.random_element(elements=('Chicken', 'Beef', 'Pork', 'Fish', 'Tofu', 'Egg'))
    elif category == 'Produce':
        item_name = fake.random_element(elements=('Apple', 'Banana', 'Pear', 'Grapes', 'Berries', 'Carrot', 'Celery', 'Green pepper', 'Red pepper', 'Onion'))
    else:
        item_name = fake.random_element(elements=('Ketchup', 'Mustard', 'Relish', 'Mayo', 'Salad dressing'))

    quantity = random.randint(1, 1000)  # Random quantity between 1 and 1000
    residence_name = fake.random_element(elements=('Delaware Hall', 'Medway-Sydenham Hall', 'Saugeen-Maitland Hall', 'Alumni House', 'Elgin Hall', 'Essex Hall', 'Lambton Hall', 'London Hall', 'Bayfield Hall', 'Ontario Hall', 'Clare Hall', 'Perth Hall'))
    last_update_date = date.today()  # Current date

    return (
        item_id,
        item_name,
        category,
        quantity,
        residence_name,
        last_update_date
    )

# Function to insert data into the database
def insert_equipment_data(cursor, equipment_data):
    insert_query = """
    INSERT INTO cafinventory 
    (Item_ID, Item_Name, Category, Quantity, Residence_Name, Last_Update_Date)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, equipment_data)

def main():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='', # replace with your password
        database='test'  # Replace 'test' with your actual database name if different
    )
    cursor = conn.cursor()

    fake = Faker()
    num_items = 20  # Number of entries to insert into the table

    for _ in range(num_items):
        equipment_data = generate_equipment_data(fake)
        insert_equipment_data(cursor, equipment_data)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()