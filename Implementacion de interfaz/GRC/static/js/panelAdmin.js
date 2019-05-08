
$(document).ready(function(){
    console.log("Bienvenido Administrator");
    pedirUsuariosSinValidar()
    
    console.log("ahi te los traje my frien")
});

$(document).on('click', ".icon-ok", function() {
    console.log("Valida a " + $(this).data("email"));
    validarUsuario($(this).data("email"));
});

$(document).on('click', ".icon-cancel-1", function() {
    console.log("Rechaza a " + $(this).data("email"));
});

function validarUsuario(emailUsuario){
    console.log("Ajax" + emailUsuario)
    $.ajax({
        url:'validarUsuario', 
        type:'POST',
        data:{
            "email": emailUsuario,
        },
        success: function(response){
            pedirUsuariosSinValidar();
            console.log("Validado");
        },
        error: function(response){
            console.log("ALgun Error");
        },
    });
    console.log("Posterr")
    
};


function rechazarUsuario(emailUsuario){

};


function pedirUsuariosSinValidar(){
    $.ajax({
        
        url: "traerUsuariosSinValidar",
        
        type: "POST",
        
        data: {},
        
        success: function(response){
            $("#lstUsuarios").html("");
            for(i=0; i < response.length; i++){
                /*POR QUE FORMATO DE PROGRAMADORA Y NO DE DISEÑADORA... no?*/
                
                $("#lstUsuarios").append(`
                    <div class="solicitud`+ (i%2 + 1) +`"> 
                        <div class=""> El usuario con  mail: `+ response[i].email + ` quiere entrar al sistema </div>
                        <div class="">
                            <label id="lblAceptar` + i + `" class="icon-ok actionButton"> Aceptar </label>  
                            <label id="lblCancelar` + i + `"class="icon-cancel-1 actionButton">Rechazar</label>
                        </div>
                    </div>`
                );
                $("#lblAceptar" + i).data("email", response[i].email);
                $("#lblAceptar" + i).data("idUsuario", response[i].id);
                $("#lblCancelar" + i).data("email", response[i].email);
                $("#lblCancelar" + i).data("idUsuario", response[i].id);
                
            }
        },
        
        error: function(response){
            console.log("PierdoTODO");
            console.log(response);
        },
    });
}