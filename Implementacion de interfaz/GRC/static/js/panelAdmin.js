
$(document).ready(function(){
    console.log("Bienvenido Administrator");
    $.ajax({
        
        url: "traerUsuariosSinValidar",
        
        type: "POST",
        
        data: {},
        
        success: function(response){
            for(i=0; i < response.length; i++){
                console.log(response[i]);
                /*POR QUE FORMATO DE PROGRAMADORA Y NO DE DISEÑADORA... no?*/ 
                $("#lstUsuarios").append(`
                    <div class="solicitud`+ (i%2 + 1) +`"> 
                        <div class=""> El usuario con  mail: `+ response[i].email + ` quiere entrar al sistema </div>
                        <div class="">
                            <label class="icon-ok actionButton"> Aceptar </label>  
                            <label class="icon-cancel-1 actionButton">Rechazar</label>
                        </div>
                    </div>`
                );
            }
        },
        
        error: function(response){
            console.log("PierdoTODO");
            console.log(response);
        },
    });
    console.log("ahi te los traje my frien")
});

$(document).on('click', "#detectame123", function() {})
