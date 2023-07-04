# TFG

La industria de los videojuegos se ha convertido en una de las industrias más importantes a nivel mundial, por delante de otras industrias de entretenimiento como la música o el cine. La inteligencia artificial ha tenido un papel destacado en esta industria, permitiendo que una maquina analice información del juego, aprenda y emule el comportamiento de un ser humano. Este trabajo de fin de carrera enmarca este contexto, desarrollando 2 agentes inteligentes capaces de jugar de manera autónoma, bien como único jugador o enfrentado a un oponente humano.

El primer agente, denominado PATIG (anagrama de IAPTG, Intelligent Agent Plays Tabletop Games), es capaz de jugar al 3 y al 4 en raya. Para ello, se ha utilizado el algoritmo minimax para el calcula y la puntualización de todos los tableros, con el fin de escoger el mejor movimiento actual.
El segundo agente, que hemos denominado GRAPI (anagrama de IAPRG, Intelligent Agent Plays Retro Games), es capaz de jugar al videojuego Pong y al videojuego del dinosaurio de Google. Para ello, utiliza el algoritmo NEAT, con el cual es capaz de entrenar diferentes redes neuronales para obtener 1 que sea capaz de jugar a un alto nivel al videojuego.
Para implementar ambos agentes, ha sido necesario desarrollar los cuatro juegos de manera paralela, para que nuestros agentes sean capaces de realizar movimientos en el juego y tengas todos los datos que proveen dichos juegos a su disposición.

Los resultados experimentales los hemos dividido en 4 bloques y hemos estudiado la calidad del agente y su tiempo de respuesta.


# Estructura y contenido del proyecto.

-> 3Raya -- Proyecto para el juego 3 en raya
	-> 3raya.js: 	Archivo javascript donde esta la logica del 3 en raya y el agente
	-> index.html: 	Archivo html donde se mostrara el juego del 3 en raya y donde se podra jugar
	-> style.css: 	Archivo css para proveer de estilo a la paginal html

-> 4Raya -- Proyecto para el juego 4 en raya
	-> 4raya.js:	Archivo javascript donde esta la logica del 4 en raya y el agente
	-> index.html: 	Archivo html donde se mostrara el juego del 4 en raya y donde se podra jugar
	-> style.css: 	Archivo css para proveer de estilo a la paginal html

-> NEAT-Dino -- Proyecto para el juego del dinosaurio
	->img:  		Carpeta donde se guardan las imagenes que se utilizan en el proyecto
		->btn: 	Carpeta donde se guarda las imagenes de los botones
		->cactus:   Carpeta donde se guarda las imagenes de los cactus
		->dino:	Carpeta donde se guarda las imagenes del dinosaurio
		->ground:   Carpeta donde se guarda las imagenes de la pista por donde correr 
	->cactus.py: 	Archivo python donde esta la logica los cactus
	->config.txt: 	Archivo de configuracion utilizado en el sistema
	->dino.py:	 	Archivo python donde esta la logica de los dinosaurios
	->game.py:	 	Archivo python donde esta la logica del videojuego
	->leeme.txt: 	Archivo leeme con instrucciones para la ejecucion del videojuego
	->mejor.pickle:	Archivo binario donde se guarda un objeto de Python
	->obstaculo.py:	Archivo python con la logica de los obstaculos
	->requirements.txt: Archivo txt donde se guardan los modulos para ejecutar el proyecto

-> NEAT-Pong -- Proyecto para el juego del dinosaurio
	->img:  		Carpeta donde se guardan las imagenes que se utilizan en el proyecto
		->assets: 	Carpeta donde se guarda las imagenes
	->pong:		Carpeta donde se guarda los archivos Python del videojuego
		->init.py   Archivo python para la importacion de las clases
		->ball.py   Archivo python con la logica de la pelota
		->game.py   Archivo python con la logica del videojuego
		->paddle.py Archivo python con la logica de la raqueta
	->config.txt: 	Archivo de configuracion utilizado en el sistema
	->leeme.txt: 	Archivo leeme con instrucciones para la ejecucion del videojuego
	->mejor.pickle:	Archivo binario donde se guarda un objeto de Python
	->neat-Pong.py:	Archivo python donde lanzamos al juego con nuestro agente
	->requirements.txt: Archivo txt donde se guardan los modulos para ejecutar el proyecto