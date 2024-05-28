function userInformation(form){
    var userName = form.user.value;
    var passWord = form.pass.value;
    var url = '/user?inputData=' + encodeURIComponent(userName) + ' ' + encodeURIComponent(passWord)
    window.location.href = url;
}

function loginFailed(){
    var params = new URLSearchParams(document.location.search);
    var flash = params.get("loginMessage");
    if( flash == "True" ){
        alert("Login attempt failed, please try again.")
    }
}