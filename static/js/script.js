document.addEventListener("DOMContentLoaded", function() {
    let spinner = document.getElementById("spinner");
    spinner.style.display = "none"
})

// email user and admin when contact form is used 
function sendMail(contactForm){
    spinner.style.display = "block"
    emailjs.send("outlook", "lotr_contact", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "subject": contactForm.subject.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            contactForm.reset();
            console.log("Form is reset");
            spinner.style.display = "none"
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;
}

function newAlert() {
    alert("If you have completed the form correctly you will receive a confirmation email once the form resets!")
}

  
// email admin when user posts a recipe or comment

function adminNotification() {
    emailjs.send("outlook","lotrAPPROVE")
    .then(
        function(response) {
            console.log("SUCCESS", response);
            contactForm.reset();
            console.log("Form is reset");
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;
}

function submitAlert() {
    alert("Thank you for your submission, admin will approve it shortly if suitable")
}

function editAlert() {
    alert("You have edited a post successfully. Admin will overlook the changes to ensure they still follow community guidelines.")
}

// message handling

setTimeout(function() {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);


