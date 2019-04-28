/*Funcion que trae las referencias de un grupo*/
function pedirReferencias(idGrupoactual){
    $.ajax({
        url:'cargarListaReferencias', 
        type:'POST',
        data:{
            "grupo": idGrupoActual,
        },
        success: function(response){
            $("#lblCantidadCitas").html(String(response.length))
            $("#divContenedorReferencias").html("<div id='divSinRef' class='referencia'></div>")
            if(response.length != 0 ){
                $("#divSinRef").hide()
                for(i=0;i<response.length;i++){
                    $("#divContenedorReferencias").append(generarReferenciaHTML(response,i));
                    
                    $("#divReferenciaId"+String(response[i].id)).data('idReferencia', 
                                                                      response[i].id);
                }
            }
            else
            {

                $("#divSinRef").html("no hay ninguna cita en el grupo")
            }

        },
        error: function(response){
            console.log(response)
        },

    })
}

function primeraCarga(){
    console.log("Esto se imprime 1 vez en la primera cargas");
    $("#lblUsuarioLogueado").html(String(idUsuarioLogueado));
    $("#lblIdGrupo").html(idGrupoActual);
    $("#divPublicarReferencia").hide();
    console.log("ENTREEWEWWEWEWEWE")
}

/*Funcion que Trae los comentarios*/
function pedirComentarios(idReferenciaSel){
    $.ajax({
        url : 'cargarComentarios',
        type: 'POST',
        data:{
            'idReferencia' : idReferenciaSel,
        },
        success: function(response){
            $("#divComentrarioDeRefSinEscribir"+idReferenciaSel).html("");
            for(i=0; i < response.length; i++){
                var conteoPar = 0
                if(i % 2 == 0){
                    conteoPar = 2

                }
                else{
                    conteoPar = 1
                }
                $("#divComentrarioDeRefSinEscribir"+idReferenciaSel).append("<div class='insertarComentario"+conteoPar+"'><div class='clsComentarioGeneral'>MAthov Comento:<div class='divContenidoComentario'>"+response[i].comentario+"</div><label class='clsFechaDeComentario'>"+response[i].fecha+"</label></div></div>");
            }

        },

        error: function(response){console.log("errer")},
    });
}

/*Funcion que formatea Texto plano a HTML*/
function nlTobr (str, is_xhtml) {
    if (typeof str === 'undefined' || str === null) {
        return '';
    }
    var breakTag = (is_xhtml || typeof is_xhtml === 'undefined') ? '<br />' : '<br>';
    return (str + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1' + breakTag + '$2');
}

/*Funcion que formatea el HTML para la DIV*/
function generarReferenciaHTML(rta,i){
    var prueba = `
    <div class='referencia' id='divReferenciaId`+String(rta[i].id)+`'>
        <div class='divEncabezado'>
            <div class='fizquierda' >Fecha:`+rta[i].fecha+`</div>
            <div class='fderecha'>`+rta[i].descripcion+`</div>
        </div><br><br>
        <label>`+rta[i].cita+`</label><br>
        <div class='divPiePagina'>
            <div class='divUsuario'>`+rta[i].usuario+`</div>
            <div class='divLink'> Link: `+rta[i].link+`</div>
            <div class='divIconComentario' id='btnComentario`+String(rta[i].id)+`'>
            </div>
        </div>  
    </div>
    <div id='divComentrarioDeRef`+rta[i].id+`' class='refDeCom insertarComentario'>
        <div class='insertarComentario'>
            <div>Escribi tu Comentario:<br>
                <textarea id='textComentario`+rta[i].id+`'rows = '5' cols = '60' class='textComentario'>
                </textarea>
                <button id='btnComentar`+rta[i].id+`' class='btn btn-primary btnClsComentar'>Comentar</button>
            </div>
        </div>
        <div class='clsDivComentarioSinEscribir' id='divComentrarioDeRefSinEscribir`+rta[i].id+`'></div>
    </div>
`
    return prueba;
    /*
    return "<div class='referencia' id='divReferenciaId"+String(rta[i].id)+"'><div class='divEncabezado'><div class='fizquierda' >Fecha:"+rta[i].fecha+"</div><div class='fderecha'>"+rta[i].descripcion+"</div></div><br><br><label>"+rta[i].cita+"</label><br><div class='divPiePagina'><div class='divUsuario'>"+rta[i].usuario+"</div><div class='divLink'> Link: "+rta[i].link+"</div><div class='divIconComentario' id='btnComentario"+String(rta[i].id)+"'></div></div></div><div id='divComentrarioDeRef"+rta[i].id+"' class='refDeCom'><div class='insertarComentario'><div>Escribi tu Comentario:<br><textarea id='textComentario"+rta[i].id+"'rows = '5' cols = '60' class='textComentario'></textarea><button id='btnComentar"+rta[i].id+"' class='btn btn-primary btnClsComentar'>Comentar</button></div></div><div class='clsDivComentarioSinEscribir' id='divComentrarioDeRefSinEscribir"+rta[i].id+"'></div></div>"*/
}


function tstResponse(){
    $.ajax({
        url: 'traerR',
        type: 'POST',
        data:{

        },
        success: function(response){
            console.log("dale bien");
            console.log(response)},
        error:  function(response){
            console.log("dale putooo");
            console.log(response)},
    });
}
function agregarGrupo(){
    console.log("Creando Grupo:", idUsuarioLogueado)
    $.ajax({
        url: 'crearGrupo',
        type: 'POST',
        data:{
            "nombreGrupo": $("#txtNombreDelGrupo").val(),
            "descripcion": $("#txtDescripcionDelGrupo").val(),
            "usuarioCredor": idUsuarioLogueado,
        },
        success: function(response){
            console.log("bien")
            console.log(response)
        },
        error: function(response){
            console.log("bien PERO CON ERROS")
            console.log(response)
        },
    });
}

function publicarReferencia(){
    var aHTML = $('#summernote').summernote("code"); //save HTML If you need(aHTML: array).
    console.log(aHTML);

    if($("#descripcion").val() == "" || $("#descripcion").val().localeCompare("Escriba aqui") == 0){
      alert("Debe ingresar una descripcion");
    }
    else if($("#link").val() == "" || $("#link").val().localeCompare("Escriba aqui") == 0){
      alert("Debe ingresar un link");
    }
    else{
        console.log("este es mi json")
        console.log("idUsuarioLogueado: ", idUsuarioLogueado)
        console.log("grupo: ", idGrupoActual)
        console.log(aHTML)
        console.log("descripcion:",$("#descripcion").val())
        console.log("link: ",$("#link").val())
        console.log("tags:", "algo")
        $.ajax({
            url : "publicarReferencia",
            type : "POST",
            data : {
              usuario : idUsuarioLogueado,
              grupo : idGrupoActual,
              cita : aHTML,
              descripcion : $("#descripcion").val(),
              link : $("#link").val(),
              tags : "algo",
            },
            success: function(response){
                $("#divPublicarReferencia").hide();
                pedirReferencias(idGrupoActual);
            },
            error: function(response){
                alert("Error al cargar la referencia");
            }
        });
    }
}

function invitarUsuarioAGrupo(){
    console.log("Invitando a:", $("#txtMailDeUsuario").val(), "al grupo:", idGrupoActual);
    $.ajax({
        url: 'invitarUsuario',
        type: 'POST',
        data: {
            "mailDeUsuario": $("#txtMailDeUsuario").val(),
            "idDelGrupo": idGrupoActual,
            "permisoUsuario": "lectura",

        },
        success: function(response){
            console.log("Bien, Revisa el response")
            console.log(response)
        },
        error: function(response){
            console.log("Mal, Rev Resp")
            console.log(response)
        }
    });

}




/*
    DOCUMENT READY
*/
$(document).ready(function(){

    $('#summernote').summernote({
        height: '300px',
        width: '600px',
        focus: true,
        lang: 'es-ES',
        toolbar: [
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['fontsize', ['fontsize']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['height', ['height']],
        ['insert', ['link']],
        ]
    });

    $("#btnEnviar").click(publicarReferencia);
    $("#btnCrearGrupo").click(agregarGrupo);

    $("#btnTST").click(tstResponse);

    $("#btnInvitarUsuario").click(invitarUsuarioAGrupo)

    misCookies = document.cookie
    listaCookies = misCookies.split(";")
    for (i in listaCookies) {
        busca = listaCookies[i].search("idUsuarioLogueado");
        if (busca > -1) {
            micookie=listaCookies[i]
            igual = micookie.indexOf("=");
            valor = micookie.substring(igual+1);
            idUsuarioLogueado = valor;
        }
    }
    primeraCarga();

    $("body").on("click",".btnGrupos",function(){
        document.cookie = "idGrupoLogueado=" + this.id.substring(this.id.indexOf("=")+1);
        window.location.href = ('http://localhost:5000/inicio')
    });


    $.ajax({
        async: true,
        data : {
            "usuario" : valor,
        },
        url : "cargarListaGrupo",
        type : "POST",
        beforeSend : function() {
            $('#gruposLista').html("Cargando Grupos");
        },
        success : function(response) {
            $('#gruposLista').html(response);
            uDataGlobal = response[0];
            console.log(response);
            $("#columnaIzquierda").append('<br><img id = "IMGagregar" div="grupoFoto" class="img-circle GrupIMG" src="https://image.flaticon.com/icons/svg/25/25340.svg" alt="Generic placeholder image" width="50" height="50"><br>'+ "AGREGAR");
            if(response[0]==null){
                console.log("SOY NULL");
            }
            else{
                for(i=0; i < response[0].length; i++){
                var nombre = response[0][i][1]
                if(nombre.length > 7){
                    nombre = response[0][i][1].slice(0, 5) + "..."
                }

                $("#columnaIzquierda").append('<br><img id = "IMG'+String(i)+'" div="grupoFoto" class="img-circle GrupIMG" src="https://images.emojiterra.com/google/android-oreo/512px/1f625.png" alt="Generic placeholder image" width="50" height="50"><br>'+ nombre);
                $("#IMG"+i).data('idNecesario', String(response[0][i][0]));    
                $("#IMG"+i).data('idGrupo', String(response[0][i][0]));
                $("#IMG"+i).data('elNombre', String(response[0][i][1]));
                $("#IMG"+i).data('laDescripcion', String(response[0][i][2]));
                $("#IMG"+i).data('posEnArray', i);

                $("#IMG"+i).tooltip({title: String(response[0][i][2]), trigger: "hover", placement: "right"});
                }
            }

        },
        error : function(response) {
            $('#divUsuarioSinGrupo').show()
            $.ajax({
                async: true,
                url: "traerTodosGrupos",
                success: function(response){
                    $('#lblCantGrupos').text(response.length);
                    console.log(response);
                    var opcion = document.createElement("option");
                    $('#lstGrupos').empty();
                    opcion.text = "Seleccione un grupo"
                    opcion.value = "vacio"
                    $('#lstGrupos').append(opcion);
                    for (i = 0; i < response.length;i++){
                        var opcion = document.createElement("option");
                        opcion.text = response[i][1];
                        opcion.value = i
                        $('#lstGrupos').append(opcion);
                        console.log("Agregando: ", response[i][1])
                    }
                },
                error: function(response){alert("error")}
            });

        }
    });

});


/*
    Click en nueva Publicacion
*/
$(document).on('click', "#detectame123", function() {
    console.log("click DETECATADO")
    $("#divPublicarReferencia").show();
});
/* Click en Boton ComentAr*/
$(document).on('click', ".btnClsComentar", function() {
    var idA = $(this).parents(".refDeCom").prev().data("idReferencia")
    $.ajax({
        url: 'comentarReferencia',
        type: 'POST',
        data:{
            'idReferencia' : idA,
            'comentario' : nlTobr($("#textComentario"+idA).val()),
            'idUsuario' : idUsuarioLogueado,
        },
        success: function(response){
            $("#textComentario"+idA).val("");
            pedirComentarios(idA);
        },
        error: function(response){console.log("error")},
    });

});
/*Click en COMENTARIO*/
$(document).on('click', ".divIconComentario", function() {
    console.log($(this).parents(".referencia").data('idReferencia'))
    var idReferenciaSel = $(this).parents(".referencia").data('idReferencia')
    pedirComentarios(idReferenciaSel);


    if($("#divComentrarioDeRef"+idReferenciaSel).hasClass("mostrar")){
        $("#divComentrarioDeRef"+idReferenciaSel).removeClass("mostrar")
    }

    else{
        $("#divComentrarioDeRef"+idReferenciaSel).addClass("mostrar")
    }

});

/*Click en BARRA DE GRUPOS*/
$(document).on('click', ".GrupIMG", function() {
    $("#divPublicarReferencia").hide();
    $('#lblNombreGrupo').html("_"+$(this).data('elNombre')+"");
    $('#lblDescripcionGrupo').html("_"+$(this).data('laDescripcion')+"");
    $('#lblIdGrupo').html("_"+$(this).data('idGrupo'));
    $("#lblPermisoEnGrupo").html(uDataGlobal[$(this).data('posEnArray')][3])
    idGrupoActual = $(this).data('idGrupo');
    if($(this).attr('id') == "IMGagregar"){
        console.log("CLICKITO");
        if($('#divAgregarGrupo').is(':visible')){
            $('#divAgregarGrupo').hide();
        }
        else{
            $('#divAgregarGrupo').show();
        }
    }
    else{
        $('#divAgregarGrupo').hide();
        if(uDataGlobal[$(this).data('posEnArray')][3] == 'creador'){
            $('#divAdminGrupo').show();
        }
        else{

            $('#divAdminGrupo').hide();
        }
        if(uDataGlobal[$(this).data('posEnArray')][3] == 'lectura'){
            document.getElementById("detectame123").style.visibility = "hidden";
            console.log("Oculta")
        }
        else{
            document.getElementById("detectame123").style.visibility = "visible";
            console.log("Muestra")
        }
    }
    pedirReferencias(idGrupoActual);
});