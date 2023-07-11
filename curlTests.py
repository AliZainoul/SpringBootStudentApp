import requests
import random
import re
from faker import Faker
from datetime import datetime

# Base URL for the API
base_url = 'http://localhost:8080'

# Create an instance of Faker
fake = Faker()

# Function to generate a random first name
def generate_random_first_name():
    return fake.first_name()

# Function to generate a random last name
def generate_random_last_name():
    return fake.last_name()

# Function to generate a random student age
def generate_random_age():
    return random.randint(18, 25)

# Function to print in green
def print_green(message):
    print(f'\033[32m[SUCCESS][{datetime.now()}] {message}\033[0m')

# Function to print in red
def print_red(message):
    print(f'\033[31m[ERROR][{datetime.now()}] {message}\033[0m')

# Function to create a new student
def create_student(first_name, last_name, age):
    url = f'{base_url}/students/create'
    data = {
        'firstName': first_name,
        'lastName': last_name,
        'age': age
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print_green(f'Student {first_name} {last_name} created successfully')
    else:
        print_red(f'Failed to create student {first_name} {last_name}')

# Function to update a student
def update_student(student_id, first_name, last_name, age):
    url = f'{base_url}/students/edit/{student_id}'
    data = {
        'firstName': first_name,
        'lastName': last_name,
        'age': age
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print_green(f'Student {student_id} updated successfully')
    else:
        print_red(f'Failed to update student {student_id}')

# Function to delete a student
def delete_student(student_id):
    url = f'{base_url}/students/delete/{student_id}'
    response = requests.post(url)
    if response.status_code == 200:
        print_green(f'Student {student_id} deleted successfully')
    else:
        print_red(f'Failed to delete student {student_id}')

# Function to get existing student IDs
def get_existing_student_ids():
    url = f'{base_url}/students'
    response = requests.get(url)
    if response.status_code == 200:
        try:
            pattern = r'<td>(\d+)</td>'
            existing_student_ids = set(re.findall(pattern, response.text))
            if existing_student_ids:
                sorted_ids = sorted([int(student_id) for student_id in existing_student_ids])
                return sorted_ids
            else:
                print_red('No existing student IDs found.')
                return []
        except Exception as e:
            print_red(f'Failed to extract student IDs: {str(e)}')
            return []
    else:
        print_red('Failed to retrieve existing student IDs')
        return []






# Generate and create 50 random students
for _ in range(50):
    first_name = generate_random_first_name()
    last_name = generate_random_last_name()
    age = generate_random_age()
    create_student(first_name, last_name, age)


existing_student_ids = get_existing_student_ids()
#print(existing_student_ids)


# Delete 3 random students (with error handling)
if existing_student_ids:
    for i in range(1,4):
        delete_student_id = random.choice(existing_student_ids)
        delete_student(delete_student_id)

# Update 3 random students a random student

if existing_student_ids:
    for i in range(1,4):
        update_student_id = random.choice(existing_student_ids)
        update_student(
            update_student_id,  \
            generate_random_first_name(), \
            generate_random_last_name(),  \
            generate_random_age()
        )