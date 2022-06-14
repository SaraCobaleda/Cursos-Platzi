//scope es el alcance que tienen las variables
//hay dos tipos de scope, global y local.
//el el global van a existir todas las varibles y funciones, pero cuando se inicializa una funcion, se genera un scope local
//solo lo que esta dentro de la funcion tendra acceso a eso mismo
//en el scope local puedo acceder a una variables inicializada por fuera, pero lo global no puede acceder a lo local
var miNombre = "Sara";
function nombre(){
    var miApellido = "Cobaleda"
    console.log(miNombre + " " + miApellido);
};

nombre();