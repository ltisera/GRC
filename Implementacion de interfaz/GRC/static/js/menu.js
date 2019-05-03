/* ------------- Menu ------------- */
$(document).ready(function(){
    $("#index-main").html(inicioHTML());
});
$(document).on('click', ".menu__item", function() {
    $(".menu__item").toggleClass("menu__link--select", false);
    $(this).toggleClass("menu__link--select");
    $("#index-main").html(menuHTML($(this).attr("name")));
    $("#menu").toggleClass("mostrar");
});



/* ------------- Limpiar Coockie ------------- */

limpiameLaCoockie();

function limpiameLaCoockie(){
    document.cookie = "idUsuarioLogueado=;expires=Thu, 01 Jan 1970 00:00:01 GMT;"
}


/* ------------- Ocultar y Mostrar Nav ------------- */

$(document).on('click', "#btnMenu", function() {
    $("#menu").toggleClass("mostrar");
});


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


/* ------------- Iniciar Sesion ------------- */

$(document).on('click', "#login-submit", function() {
    if($("#email").val() == ""){
        alert("Debe ingresar usuario");
    }
    else if($("#password").val() == ""){
        alert("Debe ingresar password");
    }
    else{
        $.ajax({
            url : "loguearUsuario",
            type : "POST",
            data : {
                usuario : $("#email").val(),
                password : $("#password").val()
            },
            success: function(response){
                console.log(response);
                var idUsuarioLogueado = response.id;
                document.cookie = "idUsuarioLogueado=" + idUsuarioLogueado;
                window.location.href = ('http://localhost:5000/grupos')
                
            },
            error: function(response){
                alert(response.responseJSON.error);
            }
        });
    }

});


/* ------------- Menu HTML ------------- */

function menuHTML(opcion){
    var html = "";
    if (opcion == "inicio"){
        html = inicioHTML();
    }
    else if (opcion == "info") {
        html = infoHTML();
    }
    else if (opcion == "contacto"){
        html = "";
    }
    return html;
}

function inicioHTML(){
    var html = `
    <section class="banner">
        <img src="/banner-inicio.jpg" alt="" class="banner__img">
        <div class="banner__content banner__card banner__width">
            <h2 class="banner__title">Login</h2>
            <label class="banner__txt">Usuario: </label>
            <input class="banner__input" id="email" type="text"></p>
            <label class="banner__txt">Password: </label>
            <input class="banner__input" id="password" type="password"></p>
            <button class="banner__btn" id="login-submit">Entrar</button>
        </div>
    </section>
    <section class="group group--color">
        <div class="container">
            <h2 class="main__title">bienvenido</h2>
            <p class="main__txt">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aliquam error sint optio alias minus, nisi officia, aperiam dignissimos molestias necessitatibus. Temporibus, possimus laudantium sunt. Veniam voluptatum laudantium natus enim.</p>
        </div>
    </section>
    <section class="group main__about__description">
        <div class="container">
            <h3 class="group__title">Otro Algo</h3>
            <p">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam unde error quod voluptatum non, architecto quisquam, voluptatibus numquam distinctio necessitatibus illum ducimus? Molestiae, architecto, dolores nam quidem laboriosam corporis nulla.</p>
        </div>
    </section>
    `;
    return html;
}

function infoHTML(){
    var html = `
    <section class="banner">
        <img src="/banner-info.jpg" alt="" class="banner__img">
        <div class="banner__content" style="width:90%">
            <h2 class="banner__title banner_info_title">Trayendo problemas a todas sus soluciones</h2>
        </div>
    </section>
    <section class="group group--color">
        <div class="container">
            <h2 class="main__title">Sobre Nosotros</h2>
            <p class="main__txt">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sint dolore ab obcaecati animi cumque voluptate, quos id quod atque repellat, consequuntur eum eos facere et necessitatibus nisi doloremque corporis sunt. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quasi iusto nemo ducimus architecto eos earum numquam nobis a ullam tempore alias nesciunt voluptates, modi vero enim minima. Perspiciatis, rerum! Dolor! Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil asperiores quaerat itaque rem temporibus deleniti dolor iste fugiat, minima natus perspiciatis sed! Magnam ipsum totam sit dolorem nostrum, reiciendis modi.</p>
        </div>
    </section>
    <section class="group our-team">
        <h2 class="group__title">Nuestro Equipo</h2>
        <div class="container container--flex">
            <div class="column column--33">
                <h3 class="our-team__title">Bongo</h3>
                <img src="/team1.jpg" alt="" class="our-team__img our-team__txt">
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Explicabo, fugiat, a repudiandae reiciendis architecto deserunt optio rerum earum error natus ad cumque labore blanditiis nobis nihil aliquam dolor iste voluptate.</p>
            </div>
            <div class="column column--33">
                <h3 class="our-team__title">Tio Cosa</h3>
                <img src="/team2.jpg" alt="" class="our-team__img our-team__txt">
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Maxime reiciendis, sapiente minima vitae praesentium blanditiis officia minus, laudantium culpa ut quae in, animi numquam. Placeat omnis dolores deserunt architecto quo.</p>
            </div>
            <div class="column column--33">
                <h3 class="our-team__title">Carlos</h3>
                <img src="/team3.jpg" alt="" class="our-team__img our-team__txt">
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut vero ea quae, rem culpa, nostrum quos similique dignissimos voluptas beatae, quaerat cupiditate atque cumque enim provident animi! At, distinctio, quo.</p>
            </div>
        </div>
    </section>
    `;
    return html;
}