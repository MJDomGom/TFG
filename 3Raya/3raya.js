var tablero = [0, 0, 0, 0, 0, 0, 0, 0, 0];
var jugadorP = 1;
var jugadorIA = 2;
var turnoActual = jugadorP;
var juegoActivo = true;



function dibujar() {
    for (i = 0; i < tablero.length; i++) {
        if (tablero[i] == 0) {
            document.getElementById("c" + i).style.backgroundColor = "white";
        } else {
            if (tablero[i] == jugadorP) {
                document.getElementById("c" + i).style.backgroundColor = "red";
            } else {
                if (tablero[i] == jugadorIA) {
                    document.getElementById("c" + i).style.backgroundColor = "blue";
                }
            }
        }
    }
}

function selecCasilla(casilla) {
    if (juegoActivo == true) {
        if (tablero[casilla] == 0) {
            if (turnoActual == jugadorP) {
                tablero[casilla] = jugadorP;
                disponibles = casillasDisponibles();
                dibujar();
                let isGanador = comprobarGanador();
                if (disponibles > 1 && isGanador == false) {
                    //movRanIA();
                    mejorMov();
                }
            }
        } else {
            window.alert("No puedes pulsar sobre una casilla coloreada");
        }
        dibujar();
        comprobarGanador();
    }
}

function comprobarGanador(){
    var ganador = checkGanador();
    switch (ganador) {
        case 0:
            return false;
            break;
        case 1:
            document.getElementById("resultado").innerHTML = '<span><h3>Gano la persona</h3></span>';
            juegoActivo = false;
            return true;
            break;
        case 2:
            document.getElementById("resultado").innerHTML = '<span><h3>Gano la IA</h3></span>';
            juegoActivo = false;
            return true;
            break;
        case 3:
            document.getElementById("resultado").innerHTML = '<span><h3>Empate</h3></span>';
            juegoActivo = false;
            return true;
            break;
    }
}

function checkGanador() {
    var espacios = 0
    for (i = 0; i < tablero.length; i++) {
        if (tablero[i] == 0) {
            espacios++;
        }
    }
    //HORIZONTAL
    if (tablero[0] == tablero[1] && tablero[1] == tablero[2] && tablero[0] != 0) { return tablero[0]; }
    if (tablero[3] == tablero[4] && tablero[4] == tablero[5] && tablero[3] != 0) { return tablero[3]; }
    if (tablero[6] == tablero[7] && tablero[7] == tablero[8] && tablero[6] != 0) { return tablero[6]; }
    //VERTICAL
    if (tablero[0] == tablero[3] && tablero[3] == tablero[6] && tablero[0] != 0) { return tablero[0]; }
    if (tablero[1] == tablero[4] && tablero[4] == tablero[7] && tablero[1] != 0) { return tablero[1]; }
    if (tablero[2] == tablero[5] && tablero[5] == tablero[8] && tablero[2] != 0) { return tablero[2]; }
    //DIAGONAL
    if (tablero[0] == tablero[4] && tablero[4] == tablero[8] && tablero[0] != 0) { return tablero[0]; }
    if (tablero[2] == tablero[4] && tablero[4] == tablero[6] && tablero[2] != 0) { return tablero[2]; }

    if (espacios > 0) {
        return 0;
    } else {
        return 3;
    }
}

function movRanIA() {
    casilla = 1;
    while (casilla != 0) {
        random = Math.floor(Math.random() * 10);
        if (tablero[random] == 0) {
            tablero[random] = jugadorIA;
            casilla = 0;
        }
    }
}
function casillasDisponibles() {
    count = 0;
    for (i = 0; i < tablero.length; i++) {
        if (tablero[i] == 0) {
            count++;
        }
    }
    return count;
}

function mejorMov() {
    let mejorPuntuacion = -Infinity;
    let mejorCasilla;
    for (let i = 0; i < tablero.length; i++) {
        if (tablero[i] == 0) {
            tablero[i] = jugadorIA;
            let puntuacion = minimax(tablero, 0, false);
            tablero[i] = 0;
            if (puntuacion > mejorPuntuacion) {
                mejorPuntuacion = puntuacion
                mejorCasilla = i
            }
        }
    }
    tablero[mejorCasilla] = jugadorIA
}


//NO ESTA COGIENDO EL NUEVO TABLERO CADA VEZ QUE HACE LA FUNCION RECURSIVA
function minimax(tablero, profundidad, isMax) {
    let resultado = checkGanador(tablero);
    if (resultado == 1) {
        return -1;
    } else {
        if (resultado == 2) {
            return 1;
        } else {
            if (resultado == 3) {
                return 0;
            }
        }
    }
    if (isMax == true) {
        let mejorPuntuacion = -Infinity;
        for (let i = 0; i < tablero.length; i++) {
            if (tablero[i] == 0) {
                tablero[i] = jugadorIA;
                let puntuacion = minimax(tablero, profundidad + 1, false);
                tablero[i] = 0;
                if(puntuacion > mejorPuntuacion){mejorPuntuacion = puntuacion}
            }
        }
        return mejorPuntuacion;
    } else {
        let mejorPuntuacion = Infinity;
        for (let i = 0; i < tablero.length; i++) {
            if (tablero[i] == 0) {
                tablero[i] = jugadorP;
                let puntuacion = minimax(tablero, profundidad + 1, true);
                tablero[i] = 0;
                if(puntuacion < mejorPuntuacion){mejorPuntuacion = puntuacion}
            }
        }
        return mejorPuntuacion;
    }
}


