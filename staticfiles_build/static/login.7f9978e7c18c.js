let showpassword = document.getElementById("showpassword");
let password = document.getElementById("password");

showpassword.addEventListener("click", function () {
    if (password.type === "password") {
        password.type = "text";
    } else {
        password.type = "password";
    }
});

