$(document).ready(function(){
    limpiameLaCoockie();
    
    /*$("#register-submit").click(function(){
        registrarUsuario();
    });*/
});

function limpiameLaCoockie(){
    document.cookie = "idUsuarioLogueado=;expires=Thu, 01 Jan 1970 00:00:01 GMT;"
}

/*
function registrarUsuario(){
    if($("#apellido").val() != "" &&
       $("#nombre").val() != "" &&
       $("#emailr").val() != "" &&
       $("#passwordr").val() != "" &&
       $("#confirm-password").val() != ""){
        console.log($("#apellido").val());
        console.log($("#nombre").val());
        console.log($("#emailr").val());
        console.log($("#passwordr").val());

        $.ajax({
            url : "crearUsuario",
            type : "POST",
            data : {
                apellido : $("#apellido").val(),
                nombre : $("#nombre").val(),
                email : $("#emailr").val(),
                password : $("#passwordr").val()
            },
            success: function(response){
                console.log(response);
                alert("Bien");
            },
            error: function(response){
                console.log("Error en algo");
            }
        });
    }
    else{
        alert("Completa todos los campos");
    }
}
*/

/* ------------- Ocultar y Mostrar Nav ------------- */
var btnMenu = document.getElementById("btnmenu");
var menu = document.getElementById("menu");
btnMenu.addEventListener("click", function(){
	"use strict";
	menu.classList.toggle("mostrar");
});

/* ------------- Iniciar Sesion ------------- */

var btnLogin = document.getElementById("login-submit");
btnLogin.addEventListener("click", function(){
	"use strict";
    if(document.getElementById("email").value == ""){
        alert("Debe ingresar usuario");
    }
    else if(document.getElementById("password").value == ""){
        alert("Debe ingresar password");
    }
    else{
        $.ajax({
            url : "loguearUsuario",
            type : "POST",
            data : {
                usuario : document.getElementById("email").value,
                password : document.getElementById("password").value
            },
            success: function(response){
                console.log(response);
                var idUsuarioLogueado = response.id;
                console.log(idUsuarioLogueado);
                document.cookie = "idUsuarioLogueado=" + idUsuarioLogueado;
                window.location.href = ('http://localhost:5000/grupos?'+idUsuarioLogueado)
            },
            error: function(response){
                alert("usuario o contraseña incorrectos");
            }
        });
    }

});


