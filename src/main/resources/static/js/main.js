// Function to handle form submission for creating a new student
function createStudent() {
    var form = document.getElementById("studentForm");

    // Get the input values
    var firstName = form.firstName.value;
    var lastName = form.lastName.value;
    var age = form.age.value;

    // Create the student object
    var student = {
        firstName: firstName,
        lastName: lastName,
        age: age
    };

    // Send a POST request to the server to create a new student
    fetch("/students/create", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(student)
    })
    .then(function(response) {
        if (response.ok) {
            // If the request was successful, redirect to the students page
            window.location.href = "/students";
        } else {
            // Display an error message
            alert("Failed to create student.");
        }
    })
    .catch(function(error) {
        console.log(error);
    });
}

// Function to handle form submission for updating a student
function updateStudent(id) {
    var form = document.getElementById("studentForm");

    // Get the input values
    var firstName = form.firstName.value;
    var lastName = form.lastName.value;
    var age = form.age.value;

    // Create the updated student object
    var updatedStudent = {
        id: id,
        firstName: firstName,
        lastName: lastName,
        age: age
    };

    // Send a POST request to the server to update the student
    fetch("/students/edit/" + id, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(updatedStudent)
    })
    .then(function(response) {
        if (response.ok) {
            // If the request was successful, redirect to the students page
            window.location.href = "/students";
        } else {
            // Display an error message
            alert("Failed to update student.");
        }
    })
    .catch(function(error) {
        console.log(error);
    });
}

// Function to handle form submission for deleting a student
function deleteStudent(id) {
    // Send a POST request to the server to delete the student
    fetch("/students/delete/" + id, {
        method: "POST"
    })
    .then(function(response) {
        if (response.ok) {
            // If the request was successful, redirect to the students page
            window.location.href = "/students";
        } else {
            // Display an error message
            alert("Failed to delete student.");
        }
    })
    .catch(function(error) {
        console.log(error);
    });
}
