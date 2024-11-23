from faker import Faker
import mysql.connector
import random


# ensuring student IDs are unique (not necessary, the Student_ID attribute in the Student table is the primary key, so tuples with the same Student_ID value cannot be added to the table)
used_ids = set()


# function to generate unique student IDs; student IDs generated are in the range of 100000000 to 999999999

def generate_unique_student_id():
    while True:
        student_id = random.randint(100000000, 999999999)
        if student_id not in used_ids:
            used_ids.add(student_id)
            return student_id


# for each student ID generated, a set of student data is generated - this includes all remaining attributes in the Student table  

def generate_student_data(fake):
    student_id = generate_unique_student_id()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name[0].lower()}{last_name.lower()}@uwo.ca"
    gender = fake.random_element(elements=('male', 'female'))
    major = fake.random_element(elements=('Arts and Humanities', 'Computer Science', 'Engineering', 'Family Studies and Human Development', 'Food and Nutrition', 'Health Sciences', 'Kinesiology', 'Nursing', 'Media and Communication Studies', 'Music', 'Science', 'Medial Science', 'Social Science', 'DAN Management and Organizational Studies', 'Ivey AEO', 'Medicine and Dentistry', 'Law', 'Education'))
    emergency_contact_name = fake.name()
    emergency_contact_phone = fake.phone_number()[:20] # make sure phone number generated does not exceed 20 characters 
    
    return (
        student_id,
        first_name,
        last_name,
        email,
        gender,
        major,
        emergency_contact_name,
        emergency_contact_phone
    )


# function used to insert data generated into the Student table in the database 

def insert_student_data(cursor, student_data):
    insert_query = """
    INSERT INTO Student 
    (Student_ID, First_Name, Last_Name, Email, Gender, Major, Emergency_Contact_Full_Name, Emergency_Contact_Phone_Number)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, student_data)

def main():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='', # replace with your password
        database='test'
    )
    cursor = conn.cursor()

    fake = Faker()
    num_students = 2000  # num_students specifies number of students to be added to the Student table  

    for _ in range(num_students):
        student_data = generate_student_data(fake)
        insert_student_data(cursor, student_data)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()