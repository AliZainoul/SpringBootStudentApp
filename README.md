# Project Name

The project is a web application for managing student information. 🚀

## Project Description

The project aims to provide a user-friendly web application for managing student information. It allows users to perform CRUD (Create, Read, Update, Delete) operations on student records. The application provides a simple and intuitive interface for adding new students, updating existing records, and deleting students from the database.

## Features

- View a list of all students
- Add a new student
- Edit student information
- Delete a student record

## Technologies Used

- Java
- Spring Boot
- Thymeleaf
- HTML/CSS/JavaScript

## Requirements

To run the project, you need to have the following installed:

- Java Development Kit (JDK)
- Apache Maven
- Tomcat (if deploying on a separate server)

## Environment Variables

Before running the project, make sure to set the following environment variables:

- `JAVA_HOME`: Path to your Java Development Kit installation directory.
- `MAVEN_HOME`: Path to your Apache Maven installation directory.
- `CATALINA_HOME`: Path to your Tomcat installation directory (if applicable).

## Getting Started

To start a new project with the same configuration and dependencies, you can use Spring Initializr. Follow the link below:

[Spring Initializr](https://start.spring.io/#!type=maven-project&language=java&platformVersion=2.7.13&packaging=war&jvmVersion=17&groupId=com.ccc&artifactId=student&name=student&description=Student%20Management%20Application&packageName=com.ccc.student&dependencies=web,data-jpa,thymeleaf,devtools)

## Getting Started with the Project

To run the project locally, follow these steps:

1. Clone the repository: `git clone <repository_url>`
2. Navigate to the project directory: `cd project_directory`
3. Install dependencies: `mvn install`
4. Run the application: `mvn spring-boot:run`
5. Access the application in a web browser: `http://localhost:8080/students`

## Actual Tree

```
.
├── HELP.md
├── README.md
├── curlTests.py
├── mvnw
├── mvnw.cmd
├── pom.xml
└── src
    ├── main
    │   ├── java
    │   │   └── com
    │   │       └── ccc
    │   │           └── student
    │   │               ├── ServletInitializer.java
    │   │               ├── StudentApplication.java
    │   │               ├── controller
    │   │               │   └── StudentController.java
    │   │               ├── model
    │   │               │   └── Student.java
    │   │               ├── repository
    │   │               │   └── StudentRepository.java
    │   │               └── service
    │   │                   ├── StudentService.java
    │   │                   └── StudentServiceImpl.java
    │   └── resources
    │       ├── application.properties
    │       ├── static
    │       │   ├── css
    │       │   │   └── style.css
    │       │   └── js
    │       │       └── main.js
    │       └── templates
    │           ├── create.html
    │           ├── delete.html
    │           ├── edit.html
    │           ├── error.html
    │           ├── students.html
    │           └── update.html
    └── test
        └── java
            └── com
                └── ccc
                    └── student
                        └── StudentApplicationTests.java

21 directories, 23 files
```



## Usage

- Upon running the application, you will be able to access the homepage that lists all the students.
- From the homepage, you can perform various actions such as creating a new student, editing student details, and deleting a student.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


Contact: [ali.zainoul.az@gmail.com]
Made with ❤️
