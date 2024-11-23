from faker import Faker
import mysql.connector
import random


# ensuring equipment IDs are unique (the equipment_ID attribute in the equipment table is the primary key, which also ensures tuples with the same equipment_ID value are not added to the equipment table)
used_ids = set()


# function to generate unique equipment IDs

def generate_unique_equipment_id():
    while True:
        equipment_id = random.randint(1000, 9999) # equipment ID generated are within the range 1000 to 9999 
        if equipment_id not in used_ids:
            used_ids.add(equipment_id)
            return equipment_id


# for each student ID generated, a set of student data is generated - this includes all remaining attributes in the Student table  

def generate_equipment_data(fake):
    equipment_id = generate_unique_equipment_id()
 
    category = fake.random_element(elements=('Cleaning', 'School', 'Sports', 'Entertainment', 'Kitchen', 'Miscellaneous'))

    # equipment_name is based on category 
    if category == 'Cleaning':
        equipment_name = fake.random_element(elements=('Broom', 'Dustpan and brush', 'Vacuum cleaner', 'Bucket and mop', 'Drying rack', 'Window squeegee', 'Cloths'))
    elif category == 'School':
        equipment_name = fake.random_element(elements=('Calculator', 'Ruler', 'Protractor', 'Whiteboard marker', 'Scissors', 'Hole puncher', 'Stapler'))
    elif category == 'Sports':
        equipment_name = fake.random_element(elements=('Soccer ball', 'Basketball', 'Volleyball', 'Football', 'Tennis racket', 'Badminton racket', 'Frisbee', 'Yoga mat', 'Jump rope', 'Resistance band', 'Spikeball set'))
    elif category == 'Entertainment':
        equipment_name = fake.random_element(elements=('Chess set', 'Checkers', 'Monopoly', 'Scrabble', 'Clue', 'Risk', 'Jenga', 'Uno', 'Deck of cards', 'Pictionary', 'Twister'))
    elif category == 'Kitchen':
        equipment_name = fake.random_element(elements=('Blender', 'Kettle', 'Toaster', 'Utensil set', 'Cutting board', 'Measuring cup', 'Can opener', 'Mixing bowl', 'Baking sheet'))
    else:
        equipment_name = fake.random_element(elements=('Umbrella', 'Extension cord', 'Power strip', 'Phone charger', 'Laptop charger', 'Toolkit', 'Sewing kit', 'First aid kit', 'Flashlight', 'Ice pack'))

    availability_status = fake.random_element(elements=('Available', 'Unavailable'))
    residence_name = fake.random_element(elements=('Delaware Hall', 'Medway-Sydenham Hall', 'Saugeen-Maitland Hall', 'Alumni House', 'Elgin Hall', 'Essex Hall', 'Lambton Hall', 'London Hall', 'Bayfield Hall', 'Ontario Hall', 'Clare Hall', 'Perth Hall'))
    equipment_condition = fake.random_element(elements=('New', 'Good', 'Fair', 'Poor', 'Damaged', 'Broken'))


    return (
        equipment_id,
        equipment_name,
        category,
        availability_status,
        residence_name,
        equipment_condition
    )


# function used to insert data generated into the Equipment table in the database 

def insert_equipment_data(cursor, equipment_data):
    insert_query = """
    INSERT INTO Equipment 
    (Equipment_ID, Equipment_Name, Category, Availability_Status, Residence_Name, Equipment_Condition)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, equipment_data)

def main():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='', # replace with your password
        database='test'
    )
    cursor = conn.cursor()

    fake = Faker()
    num_items = 250  # num_students specifies number of students to be added to the Student table  

    for _ in range(num_items):
        equipment_data = generate_equipment_data(fake)
        insert_equipment_data(cursor, equipment_data)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()