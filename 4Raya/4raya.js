var tablero =
    [[0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]];
var x = 7;
var y = 6;
var jugadorP = 1;
var jugadorIA = 2;
var turnoActual = jugadorP;
var juegoActivo = true;
var profMaxima = 4;

function selecCasilla(casilla) {
    if (juegoActivo == true) {
        colocado = false;
        i = y - 1;
        while (colocado == false && i >= 0) {
            if (tablero[i][casilla] == 0) {
                tablero[i][casilla] = turnoActual;
                disponibles = casillasDisponibles();
                dibujar();
                //console.log(tablero);
                let isGanador = comprobarGanador();
                //isGanador = false
                if (disponibles > 0 && isGanador == false) {
                    //movRanIA();
                    var start = performance.now();
                    mejorMov();
                    var end = performance.now();
                    console.log("Tiempo de decisicion de la IA: " + (end - start));
                }
                colocado = true;
            } else {
                i--;
            }
        }

        if (colocado == false) {
            window.alert("No puedes pulsar sobre una casilla coloreada");
        }
        dibujar();
        comprobarGanador();
    }
}

function dibujar() {
    for (i = 0; i < y; i++) {
        for (j = 0; j < x; j++) {
            if (tablero[i][j] == 0) {
                document.getElementById("c" + i + "" + j).style.backgroundColor = "white";
            } else {
                if (tablero[i][j] == jugadorP) {
                    document.getElementById("c" + i + "" + j).style.backgroundColor = "red";
                } else {
                    if (tablero[i][j] == jugadorIA) {
                        document.getElementById("c" + i + "" + j).style.backgroundColor = "yellow";
                    }
                }
            }
        }
    }

}

function casillasDisponibles() {
    count = 0;
    for (i = 0; i < x; i++) {
        for (j = 0; j < y; j++) {
            if (tablero[j][i] == 0) {
                count++;
            }
        }
    }
    return count;
}


function comprobarGanador() {
    var ganador = checkGanador();
    switch (ganador) {
        case 0:
            return false;
        case 1:
            document.getElementById("resultado").innerHTML = '<span><h3>Gano la persona</h3></span>';
            juegoActivo = false;
            return true;
        case 2:
            document.getElementById("resultado").innerHTML = '<span><h3>Gano la IA</h3></span>';
            juegoActivo = false;
            return true;
        case 3:
            document.getElementById("resultado").innerHTML = '<span><h3>Empate</h3></span>';
            juegoActivo = false;
            return true;
    }
}


function checkGanador() {
    var espacios = casillasDisponibles();
    //VERTICAL
    for (i = 0; i < x; i++) {
        for (j = 0; j < y - 3; j++) {
            if (tablero[j][i] == tablero[j + 1][i] && tablero[j + 2][i] == tablero[j][i] && tablero[j + 3][i] == tablero[j][i] && tablero[j][i] != 0) {
                //console.log("Tenemos un ganador");
                return tablero[j][i];
            }
        }
    }
    //HORIZONTAL
    for (i = 0; i < x - 3; i++) {
        for (j = 0; j < y; j++) {
            if (tablero[j][i] == tablero[j][i + 1] && tablero[j][i + 2] == tablero[j][i] && tablero[j][i + 3] == tablero[j][i] && tablero[j][i] != 0) {
                //console.log("Tenemos un ganador");
                return tablero[j][i];
            }
        }
    }
    //DIAGONAL DESCENDENTE
    for (i = 3; i < x; i++) {
        for (j = 3; j < y; j++) {
            if (tablero[j][i] == tablero[j - 1][i - 1] && tablero[j - 2][i - 2] == tablero[j][i] && tablero[j - 3][i - 3] == tablero[j][i] && tablero[j][i] != 0) {
                //console.log("Tenemos un ganador");
                return tablero[j][i];
            }
        }
    }

    //DIAGONAL ASCENDENTE
    for (i = 0; i < x; i++) {
        for (j = 3; j < y; j++) {
            if (tablero[j][i] == tablero[j - 1][i + 1] && tablero[j - 2][i + 2] == tablero[j][i] && tablero[j - 3][i + 3] == tablero[j][i] && tablero[j][i] != 0) {
                //console.log("Tenemos un ganador");
                return tablero[j][i];
            }
        }
    }

    if (espacios > 0) {
        return 0;
    } else {
        return 3;
    }
}

function mejorMov() {
    let mejorPuntuacion = -Infinity
    let mejorI;
    let mejorJ;
    for (let j = 0; j < x; j++) {
        let i = y - 1;
        colocado = false;
        while (i >= 0 && colocado == false) {
            if (tablero[i][j] == 0) {
                //console.log(i, j);
                tablero[i][j] = jugadorIA;
                puntuacion = minimax(tablero, 0, false, -Infinity, Infinity);
                tablero[i][j] = 0;
                if (puntuacion > mejorPuntuacion) {
                    mejorPuntuacion = puntuacion;
                    mejorI = i;
                    mejorJ = j;
                }
                colocado = true;
            } else {
                i--;
            }
        }
    }
    tablero[mejorI][mejorJ] = jugadorIA;
}


function minimax(tablero, prof, isMax, alfa, beta) {
    let resultado = checkGanador();
    if (resultado == 1) {
        return -10000;
    } else {
        if (resultado == 2) {
            return 10000;
        } else {
            if (resultado == 3) {
                return 0;
            }
        }
    }
    if (prof > profMaxima) {
        return score();
    } else {
        if (isMax == true) {
            mejorPuntuacion = -Infinity;
            for (let j = 0; j < x; j++) {
                let i = y - 1;
                colocado = false;
                while (i >= 0 && colocado == false) {
                    if (tablero[i][j] == 0) {
                        tablero[i][j] = jugadorIA;
                        puntuacion = minimax(tablero, prof + 1, false, alfa, beta);
                        tablero[i][j] = 0;
                        if (puntuacion > mejorPuntuacion) {
                            mejorPuntuacion = puntuacion;
                        }
                        colocado = true;
                        alfa = Math.max(mejorPuntuacion, alfa);
                        if (alfa >= beta) {
                            break;
                        }
                    } else {
                        i--;
                    }
                }
            }
            return mejorPuntuacion;
        } else {
            mejorPuntuacion = Infinity;
            for (let j = 0; j < x; j++) {
                let i = y - 1;
                colocado = false;
                while (i >= 0 && colocado == false) {
                    if (tablero[i][j] == 0) {
                        tablero[i][j] = jugadorP;
                        puntuacion = minimax(tablero, prof + 1, true, alfa, beta);
                        tablero[i][j] = 0;
                        if (puntuacion < mejorPuntuacion) {
                            mejorPuntuacion = puntuacion;
                        }
                        colocado = true;
                        beta = Math.min(beta, mejorPuntuacion);
                        if (alfa >= beta) {
                            break;
                        }
                    } else {
                        i--;
                    }
                }
            }
            return mejorPuntuacion;
        }
    }
}

function score() {
    let score = 0
    //VERTICAL
    for (let i = 0; i < x; i++) {
        for (let j = 0; j < y - 3; j++) {
            if (tablero[j][i] == tablero[j + 1][i] && tablero[j + 2][i] == tablero[j][i] && tablero[j][i] != 0) {
                if (tablero[j][i] == jugadorIA) {
                    //3 piezas consecutivas
                    score += 5;
                } else {
                    if (tablero[j + 3][i] == 0) {
                        score -= 4;
                    }
                }
            } else {
                if (tablero[j][i] == tablero[j + 1][i] && tablero[j][i] != 0 && tablero[j][i] == jugadorIA) {
                    //2 piezas consecutivas
                    score += 3;
                }
            }
        }
    }
    //HORIZONTAL
    for (let i = 0; i < x - 3; i++) {
        for (let j = 0; j < y; j++) {
            if (tablero[j][i] == tablero[j][i + 1] && tablero[j][i + 2] == tablero[j][i] && tablero[j][i] != 0) {
                if (tablero[j][i] == jugadorIA) {
                    //3 piezas consecutivas
                    score += 5;
                } else {
                    if (tablero[j][i + 3] == 0) {
                        //Evitar movimientos ganadores del contrario
                        score -= 4;
                    }
                }
            } else {
                if (tablero[j][i] == tablero[j][i + 1] && tablero[j][i] != 0 && tablero[j][i] == jugadorIA) {
                    //2 piezas consecutivas
                    score += 3;
                }
            }
        }
    }
    //DIAGONAL DESCENDENTE
    for (let i = 3; i < x; i++) {
        for (let j = 3; j < y; j++) {
            if (tablero[j][i] == tablero[j - 1][i - 1] && tablero[j - 2][i - 2] == tablero[j][i] && tablero[j][i] != 0) {
                if (tablero[j][i] == jugadorIA) {
                    //3 piezas consecutivas
                    score += 5;
                } else {
                    if (tablero[j - 3][i - 3] == 0) {
                        //Evitar movimientos ganadores del contrario
                        score -= 4;
                    }
                }
            } else {
                if (tablero[j][i] == tablero[j - 1][i - 1] && tablero[j][i] != 0 && tablero[j][i] == jugadorIA) {
                    //2 piezas consecutivas
                    score += 3;
                }
            }
        }
    }

    //DIAGONAL ASCENDENTE
    for (let i = 0; i < x; i++) {
        for (let j = 3; j < y; j++) {
            if (tablero[j][i] == tablero[j - 1][i + 1] && tablero[j - 2][i + 2] == tablero[j][i] && tablero[j][i] != 0) {
                if (tablero[j][i] == jugadorIA) {
                    //3 piezas consecutivas
                    score += 5;
                } else {
                    if (tablero[j - 3][i + 3] == 0) {
                        //Evitar movimientos ganadores del contrario
                        score -= 4;
                    }
                }
            } else {
                if (tablero[j][i] == tablero[j - 1][i + 1] && tablero[j][i] != 0 && tablero[j][i] == jugadorIA) {
                    //2 piezas consecutivas
                    score += 3;
                }
            }
        }
    }
    return score;
}
