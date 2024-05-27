function userInformation(form){
    var userName = form.user.value;
    var passWord = form.pass.value;
    var url = '/user?inputData=' + encodeURIComponent(userName)
    window.location.href = url;
}