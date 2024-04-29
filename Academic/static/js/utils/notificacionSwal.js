const notificacionSwal = (titleText,text,icon,confirmButton) => {
 Swal.fire({
    titleText:titleText,
    text:text,
    icon:icon,
    confirmButton:confirmButton
 });
};