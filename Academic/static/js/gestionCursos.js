const $nombre = document.getElementById('txtcurso');
const $formulario = document.getElementById('formuariocurso');
const $creditos = document.getElementById('txtcreditos');


const btnsEliminacion = document.querySelectorAll(".btnEliminacion");

(function () { //Esta funcion se dispara apenas se carga la app
    notificacionSwal(document.title, "Cursos Cargados", "success", "Ok");

btnsEliminacion.forEach((btn) => { //Escuchador de eventos para los botones del formulario
    btn.addEventListener("click", function(e) {
        e.preventDefault()//detiene la accion
        Swal.fire({
            title: "Desea eliminar el registro seleccionado?",
            showCancelButton: true,
            confirmButtonText: "Eliminar",
            confirmButtonColor: "#d33",
            backdrop: false,
            showLoaderOnConfirm: true,
            preConfirm: () => {
                location.href = e.target.href; //confirma la redireccion de la accion para llevar a cabo la ejecucion
            },
            allowOutsideClick: () => false,
                allowEscapeKey: () => false,
        });
    });
});
})();