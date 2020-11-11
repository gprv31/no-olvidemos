function clearCongresistas(){
    $('.gallery .media.hidden').each(function() {
        $(this).removeClass("hidden");
    })
}

function filterByPartido(partido){
    $('.gallery .media').each(function() {
        if ($(this).data('partido') !== partido) {
            $(this).addClass("hidden");
        }
    })
}

function filterByNombre(nombre){
    $('.gallery .media').each(function() {
        let encontrarEn = $(this).data('nombre').split(" ").join("").toLowerCase();
        console.log(encontrarEn);
        if (encontrarEn.indexOf(nombre.toLowerCase()) === -1) {
            $(this).addClass("hidden");
        }
    })
}

function filterByVotacion(votacion){
    $('.gallery .media').each(function() {
        if ($(this).data('votacion') !== votacion) {
            $(this).addClass("hidden");
        }
    })
}