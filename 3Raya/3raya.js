var tablero = [0,0,0,0,0,0,0,0,0];
var jugadorP = 1;
var jugadorIA = 2;
var turnoActual = jugadorP;

function dibujar(){
    for(i=0;i<tablero.length;i++){
        if(tablero[i] == 0){
            document.getElementById("c"+i).style.backgroundColor="white";
        }else{
            if(tablero[i] == jugadorP){
                document.getElementById("c"+i).style.backgroundColor="red";
            }else{
                if(tablero[i] == jugadorIA){
                    document.getElementById("c"+i).style.backgroundColor="blue";
                }
            }
        }
    }
}

function selecCasilla(casilla){
    if (tablero[casilla] == 0){
        if(turnoActual == jugadorP){
            tablero[casilla] = jugadorP;
            disponibles = casillasDisponibles();
            if(disponibles >1){
                movRanIA();
            }
        }
    }else{
        window.alert("No puedes pulsar sobre una casilla coloreada")
    }
    dibujar()
    var ganador = checkGanador();
    switch(ganador){
        case 0:
            break;
        case 1:
            window.alert("Gano la persona");
            break;
        case 2:
            window.alert("Gano la IA");
            break;
        case 3:
            window.alert("Empate");
            break;
    }
}

function checkGanador(){
    var espacios = 0
    for (i=0; i< tablero.length;i++){
        if(tablero[i] == 0){
            espacios++;
        }
    }
    //HORIZONTAL
    if(tablero[0] == tablero[1] && tablero[1] == tablero[2] && tablero[0] !=0){ return tablero[0];}
    if(tablero[3] == tablero[4] && tablero[4] == tablero[5] && tablero[3] !=0){ return tablero[3];}
    if(tablero[6] == tablero[7] && tablero[7] == tablero[8] && tablero[6] !=0){ return tablero[6];}
    //VERTICAL
    if(tablero[0] == tablero[3] && tablero[3] == tablero[6] && tablero[0] !=0){ return tablero[0];}
    if(tablero[1] == tablero[4] && tablero[4] == tablero[7] && tablero[1] !=0){ return tablero[1];}
    if(tablero[2] == tablero[5] && tablero[5] == tablero[8] && tablero[2] !=0){ return tablero[2];}
    //DIAGONAL
    if(tablero[0] == tablero[4] && tablero[4] == tablero[8] && tablero[0] !=0){ return tablero[0];}
    if(tablero[2] == tablero[4] && tablero[4] == tablero[6] && tablero[2] !=0){ return tablero[2];}

    if(espacios > 0){
        return 0;
    }else{
        return 3;
    }
}

function movRanIA(){ 
    casilla = 1;

    while(casilla != 0){
        random = Math.floor(Math.random()*10);
        if(tablero[random] == 0){
            tablero[random] = jugadorIA;
            casilla = 0;
        }
    }
}
function casillasDisponibles(){
    count = 0;
    for(i=0; i< tablero.length;i++){
        if(tablero[i] == 0){
            count++;
        }
    }
    return count;
}
