function sendMail(contactForm){
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
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;
}

function newAlert() {
    alert("If you have completed the form correctly you will receive a confirmation email shortly!")
}

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