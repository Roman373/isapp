document.getElementById("btn").onclick = function () {
    var inputLogin = document.getElementById("mylogin").value;
    var inputPassword = document.getElementById("mypassword").value;
    if (inputLogin === ''|| inputPassword === "") {
        alert("Вы должны что-то написать!");
    }
    else {
        window.location.href='index.html';
    }
}