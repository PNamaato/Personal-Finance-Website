
import { initializeApp } from "firebase/app";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCf1YEN8poBd9yxxjxD4J8OyiYr7ppmdJ8",
    authDomain: "personal-finance-4e7d0.firebaseapp.com",
    projectId: "personal-finance-4e7d0",
    storageBucket: "personal-finance-4e7d0.appspot.com",
    messagingSenderId: "922641146764",
    appId: "1:922641146764:web:7f4b3c996269fe5efaeca9",
    measurementId: "G-VEWWZ8H4DQ"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

const auth = firebase.auth()
const db = firebase.database()

// register function
function UserRegister(){
    // get input fields
    var email = document.getElementById("remail").value;
    var pswd = document.getElementById("rpswd").value;

    // validate email
    if (validate_email(email) == false){
        alert("Email is not valid");
        return
    }
    //  Auth
    auth.createUserWithEmailAndPassword(email,pswd).then( function(){
        // declare user variable
        var user = auth.currentUser;

        // Add to Firebase DB
        var db_ref = db.ref()

        // create user data
        var userInfo = {
            name: getId("username"),
            enail: getId("remail"),
            pswd: getId("pswd"),
            last_login: Date.now()
        };

        db_ref.child('users/' + user.uid).set(userInfo);


        alert("User created")
    }).catch((error) => {
        // firebase alerting of errors
        var errorcode = error.code;
        var errormsg = error.message;
        alert(errormsg);
    });
}

// function SignIn(){
//     var email = document.getElementById("email").value;
//     var pswd = document.getElementById("pswd").value;
//     const sign = auth.signInWithEmailAndPassword(email, pswd);
//     sign.catch(e => alert(e.msg));
//     window.open("https://www.google.com", "_self");
// }

// document.getElementById("log-reg").addEventListener('submit', (e)=> {
//     e.preventDefault();
//     var userInfo = db.push();
//     userInfo.set({
//         name: getId("username"),
//         enail: getId("remail"),
//         pswd: getId("pswd")
//     });
//     alert("Successfully Signed Up");
//     console.log("sent");
//     document.getElementById("log-reg").reset();
// });

function getId(id){
    return document.getElementById(id).value;
}

// validate fields
function validate_email(email) {
    expression = /^[^@]+@\w+(\.\w+)+\w$/
    if (expression.test(email)== true){
        return true;
    } else {
        return false;
    }  
}


// --------------------------------------------------------------------------
// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}







