//las variabbles y las funciones se declaran antes de que se porcese cualquier tipo de codigo
//solo pasa con versiones pasadas de js,en mscript6 en adelante ya no pasa
//se declara una varible y se inicializa una variables
console.log(miNombre)
var miNombre;
miNombre = "Sara";
//con hoisting se llaman variables sin haberlas declarado e de inicializarla
//como no se inicializa la varible, le da el valor de undefined
//console.log imprime en la consola, es una funcion del navegador
//tambien hay hoisting con las funciones
hey();
function hey(){
    console.log("Hola a todos " + miNombre)
};
var miNombre = "Sara";
//si llamamos una funcion antes de declararla si se obtiene el resultado esperado, siempre y cuando las 
//variables esten declaradas e inizializadas antes
//las variables y las funciones se procesan antes de ejecutar cualquier codigo, 
//pero las funciones se declaran antes que las varibles
//una buena practica todas las variables se declaran al inicio del codigo