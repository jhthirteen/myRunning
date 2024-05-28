function userInformation(form){
    var userName = form.user.value;
    var passWord = form.pass.value;
    var url = '/user?inputData=' + encodeURIComponent(userName) + ' ' + encodeURIComponent(passWord)
    window.location.href = url;
}

function loginFailed(){
    alert("Login attempt failed. Please retry")
}