from faker import Faker
import mysql.connector
import random


# function used to retrieve the student IDs of all tuples currently in the Student table 

def get_all_student_ids(cursor):
    """
    Retrieve all Student_IDs from the Student table.
    """
    query = "SELECT Student_ID FROM Student;"
    cursor.execute(query)
    return [row[0] for row in cursor.fetchall()]


# function used to generate housing preferences for each student ID retrieved 

def generate_housing_preferences(fake, student_id):
    """
    Generate random housing preferences for a given Student_ID.
    """
    room_type = fake.random_element(elements=('Single room', 'Double room', 'Suite-Style', 'Hybrid-Style'))
    community_preference = fake.random_element(elements=('Living-Learning Community', 'Quiet', 'Social', 'None'))
    roommate_preference = fake.random_element(elements=('Random', 'Manual roommate request'))
    
    return (
        student_id,  # Foreign key from the Student table
        room_type,
        community_preference,
        roommate_preference
    )

def insert_housing_preferences(cursor, housing_data):
    """
    Insert housing preferences data into the HousingPreferences table.
    """
    insert_query = """
    INSERT INTO HousingPreferences 
    (Student_ID, Room_Type, Community_Preference, Roommate_Preference)
    VALUES (%s, %s, %s, %s);
    """
    cursor.execute(insert_query, housing_data)

def main():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='', # replace with your password
        database='test'  # Replace with your database name
    )
    cursor = conn.cursor()

    fake = Faker()

    # Step 1: Retrieve all Student_IDs from the Student table
    student_ids = get_all_student_ids(cursor)

    # Step 2: Generate and insert housing preferences for each Student_ID
    for student_id in student_ids:
        housing_data = generate_housing_preferences(fake, student_id)
        insert_housing_preferences(cursor, housing_data)

    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()