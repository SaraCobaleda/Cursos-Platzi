//hay dos tipos de coehrsiones, implicitas y explicitas
//implicitas es cuando el lenguaje ayuda y cambia de un tipo de valor a otro, por ejemplo de int a string
//explicita es la forma en la que obligamos a que un valor de un tipo cambia e un valor de otro tipo

//cohercion implicita
var a = 4 + "7";
typeof a;
//genera el numero 47 dentro del string, se estan concatenando dos strings
var b = 4 * "7";
typeof b;
//aqui regresa el nuemro 28 en formato int

//cohercion explicita
var a = 20;
var b = a + "";
console.log(b)
typeof b
//b es uns tring porque se ocncateno, pero hay una forma de hacerlo sin eso, con el metodo string
var c = String(b)
typeof c
var d = Number(c)
typeof d