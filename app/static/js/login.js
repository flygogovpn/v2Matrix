function check_longinstate(){
    tocken = localStorage.getItem('condo_tocken')
    if(tocken != null){
        //document.getElementById('logostate').innerText='用户已登陆'
        document.getElementById('Register_button').style.display="none"//已登陆则隐藏注册按钮
        document.getElementById('Login_button').style.display="none"//已登陆则隐藏登录按钮
        document.getElementById('Logout_button').style.display="block"//已登陆则显示退出按钮

        console.log("tocken不为空",tocken)
    }
    else{
        console.log("tocken为空")
        document.getElementById('Register_button').style.display="block"//未登陆则显示注册按钮
        document.getElementById('Login_button').style.display="block"//未登陆则显示登录按钮
        document.getElementById('Logout_button').style.display="none"//未登陆则隐藏退出按钮
        //document.getElementById('logostate').innerText='用户未登陆'

    }
}

function test_go(pic_id){
    var tocken = localStorage.getItem('condo_tocken')
    console.log("test_go:tocken",tocken)

    $.ajax({
        type: "POST",
        url: "/publish", //上传路径  /login_test

        contentType: false,    //不可缺
        processData: false,    //不可缺
        dataType: "json",
        headers: {'Authorization': tocken},
        success: function (data) { //debugger
        var obj = eval ("(" + data + ")");//读取json格式的数据
            alert("登录返回",obj.code,obj.token[0])
        },
    });
}

function login_go(pic_id){
    var logoin_name = document.getElementById("logoin_name");
    var logoin_password = document.getElementById("logoin_password");
    var valuemap ={'logoin_name': logoin_name.value,'logoin_password': logoin_password.value};
    console.log("logoin_name",logoin_name.value)

    $.ajax({
        type: "POST",
        url: "/login_customer", //上传路径
        data: JSON.stringify(valuemap),
        contentType: false,    //不可缺
        processData: false,    //不可缺
        dataType: "json",
        success: function (data) { //debugger
            if(data.msg == '登录成功'){
                console.log("000",data.code)
                console.log("111",data.token['access_token'])
                console.log("222",data.token['refresh_token'])
                localStorage.setItem('condo_tocken', data.token['access_token'])
                var tocken = localStorage.getItem('condo_tocken')
                console.log("33333",tocken)
                alert("login successful")
                window.location.reload();

                 //alert("登录返回",obj.token)
            }
            if(data.msg == '未找到用户'){
                alert("username not found")
                window.location.reload();
            }
            if(data.msg == '密码错误'){
                alert("password wrong")
                window.location.reload();
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log("error：",error)
            alert("上传失败，请检查网络后重试:", error);
        }
    });
}
function regist_go(pic_id){
    var register_name = document.getElementById("register_name");
    var register_number = document.getElementById("register_number");
    var register_password = document.getElementById("register_password");
    var valuemap ={'register_name': register_name.value,'register_number': register_number.value,'register_password': register_password.value};
    $.ajax({
        type: "POST",
        url: "/register_customer", //上传路径
        data: JSON.stringify(valuemap),
        contentType: false,    //不可缺
        processData: false,    //不可缺
        dataType: "json",
        success: function (data) { //debugger
            if(data.msg == '注册成功'){
              localStorage.setItem('condo_tocken', data.token['access_token'])
                var tocken = localStorage.getItem('condo_tocken')
                console.log("33333",tocken)
                alert("regist successful" )
                window.location.reload();
            }
            if(data.msg == '该手机号已存在'){
                alert("number already exist" )
                window.location.reload();
            }
            if(data.msg == '该用户名已存在'){
                alert("name already exist")
                window.location.reload();
            }
                //window.location.reload();
        },
    });
}

function login_current_state_check(){
    $.ajax({
          url: "/login_current_state_check",
          type: 'POST',
          contentType: 'application/json',
          headers: {
                    "Authorization": localStorage.getItem('condo_tocken')
                 },
          async: false,
            contentType: false,    //不可缺
            processData: false,    //不可缺
            dataType: "json",
            success: function (data) {
                if(data.ret_code == 'success'){
                    window.location.href = href="http://www.phlipinecondo.club/publish";
                }
                else{
                    console.log(data.ret_code)
                    alert('pls login first')
                    window.location.reload();
                }
            }
    })
}

function logout_go(){
    localStorage.removeItem('condo_tocken')
    window.location.reload();
}