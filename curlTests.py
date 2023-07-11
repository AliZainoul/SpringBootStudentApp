import requests
import random
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
        print(f'[SUCCESS][{datetime.now()}] Student {first_name} {last_name} created successfully')
    else:
        print(f'[ERROR][{datetime.now()}] Failed to create student {first_name} {last_name}')

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
        print(f'[SUCCESS][{datetime.now()}] Student {student_id} updated successfully')
    else:
        print(f'[ERROR][{datetime.now()}] Failed to update student {student_id}')

# Function to delete a student
def delete_student(student_id):
    url = f'{base_url}/students/delete/{student_id}'
    response = requests.post(url)
    if response.status_code == 200:
        print(f'[SUCCESS][{datetime.now()}] Student {student_id} deleted successfully')
    else:
        print(f'[ERROR][{datetime.now()}] Failed to delete student {student_id}')

# Generate and create 10 random students
for _ in range(10):
    first_name = generate_random_first_name()
    last_name = generate_random_last_name()
    age = generate_random_age()
    create_student(first_name, last_name, age)

# Update a random student
update_student(1, 'John', 'Doe', 25)


delete_student_id = random.randint(1, 10)
# Delete a random student
delete_student(delete_student_id)