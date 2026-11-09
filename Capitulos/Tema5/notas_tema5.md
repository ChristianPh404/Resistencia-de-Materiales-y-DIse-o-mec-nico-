* Calculo de desplazamientos en flexion 
sigman = -mfz \cdoty /I_z % Formula navier en flexion pura recta mf =! 0 
Q_y  + M_f ---> -mfz \cdoty / (I_z) & tau = Q \cdot S* / % formula navier y colignion

dibujo rectangulo con 1 apoyo fijo izquierda 1 articulado derecha, sen 2 figuras una normal y la otra superpuesta con deformacion se marca en ambas la fibra neutra que sigue pasando por el centro

Comprobaciones de resitencias:
 -comprobar la resistencia con tension max mayorada <= tension admisible del material
 - Deformaciones maximas < eps_lim 

 nosotros lo comprobaremos sera que lo maximo que baje la fibra neutra sea menor de cierta cantidad 
 es decir queremos calcular la ecuacion de la fibra neutra (linea roja) con la ecuacion de la linea elastica o deformada  (como es una ecuacion de una curva tendra forma polinomial, es decir y = ax+ bx^n-1 + cx....)

si tengo la y sabemos lo que ha bajado, esa y se denomina flecha o deflexion (tambien puede ser para arriba segun como pongamos las cargas) como criterio de signos si sube para arriba y + para abajo

no comprobamos elongaciones que son adimensionales, sino que la ymax sea menor que un cierto lim y se hacen sin las cargas sin mayorar (se calculara con los esfuerzos) (sin mayorar)

con el giro de la seccion podremos calcular la y max, las secciones inicales (los cortes) son verticales, despues de deformar la seccion queda con cierta inclinacion, el angulo con el que queda la secciones se le llama angulo de giro theta, si el angulo es horario <0 si es antihorario >0
punto A una vez deformado pasa a A, por bernouilli como el punto tiene que ser perpendicular a la directriz antes de la deformacion despues tambien tiene que serlo, si trazamos una perpendicular en la figura inicial y luego otra en el punto de la imagen deformada es decir en A'(que seria algo mas abajo)  se puede ver entre ambas rectas el angulo de giro, 
tambien se puede medir haciendo una horizontal que pase por A' y corte con su perpendicular y ese angulo representar en la derecha tambien sera theta_A
representar una figura en un apoyo fijo recta a la derecha , si se pone una carga se deforma haciendo un arco a la derecha si hacemos una horizontal en un punto x para su x' que es el punto que pertenece a la curva con la tangente del angulo theta como es algo muy pequeño se asume que es un triangulo con su pared opuesta dy  es decir tg theta = dy/d = y' cuando los angulos son muy pequeños angulo y tang se aproximan por lo que la pendiente de la tangente es aprox el angulo de giro 

1/rho se define como la curvatura que es k  = mf/E\cdotI , E\cdotI es el modulo de rigidez 
k < 0 es curva hacia arriba > 0 es curva hacia abajo , la curvatura se obtiene con la segunda derivada de la ecuacion de la linea 22 , 
EDE ecuacion diferencial de la elastica, y'' = m_fz = EI_z 

se resuelve de la siguiente manera 
1) poner la ecuacion diferencial y integrar a ambos lados por dx % se obtiene y' 
 y' = int m_f/E \cdot I dx + c1 % como es una constante indefinida tiene constante de integracion 
2)se vuelve a integrar  
y = int y' dx = int(int m_f/E \cdot I dx + c1) dx = int int m_f/E \cdot I dx + c1X + C2

para resolver hay que dar condiciones de contorno  las condiciones son
y(x=0) = 0 ya que en los apoyos ni sube ni baja 
y(x=l) = 0  por que es el otro apoyo 

ejercicio

carga linealmente distribuida 10kn/m  apoyo fijo izquierda derecha movil distancia de viga 4m 
1) calcular las reacciones que son 20 y 20 kn 
2) calcular los momentos con la ley de momentos flectores
mfz= 20x-5x^2
3) poner la ecuacion diferencial de la elastica
y'' = m_fz = EI_z  ---> y'' = -20x-5x^2 / EI % seguramente la inercia la tendremos que calcular y la E vendra dada en este problema EI = 10kn

al integrar 
y' =int  y''dx =int(-20x-5x^2/EI )dx = 1/EI ( 20x^2/2 - 5x^3/3 + c1) % esto sera aproximadamente el angulo de giro 
4) 
volvemos a integrar 
y = int y'dx = int 1/EI ( 20x^2/2 - 5x^3/3 + c1) dx = 1/EI ( 10x^3/3 -5/3* x^4/4 + c1x +c2)
5) damos las condiciones de contorno
y (x= 0)= 0 -->1/EI ( 10*0 -5/3*0 + c1*0 +c2)=0  ---> c2 = 0---> 
y(x=4)=0  --->1/EI (10*4^3/3 - 5*4^4/12 + c1*4 +c2) ---> c1 = -26.6


6)calcular desplazamiento maximo
para ello 
 - dibujar los diagramas que se habian visto antes es decir N Q y M_f
 -dibujar debajo de esos y' que era 1/EI ( 20x^2/2 - 5x^3/3 -26.6) (se dan valores a los extremos )
 - debajo de la y' dibujamos 1/EI ( 10x^3/3 -5/3* x^4/4 -26.6)(dando valores en los extremos del intervalo) 

 para no dar puntos hacemos uso de las curvaturas 
 tenemos que la k = y'' mf/EI % (EI es siempre positivo por lo que y'' es proporcional al momento flector)

por lo que si miramos el diagrama de Mf podemos saber como es la curvatura , es decir dibujamos la misma curvatura que en mf para dibujar la y' deberia hacer tambien la segunda derivada pero como el cortante es la derivada del momento flector sabemos que es proporcional a la segunda derivada de y' es decir y''' por lo que sabemos que la curvatura de 0 a 2 es concava y de 2 a 4 es convexa hasta -26.6 el que pase por 0 es casualidad, lo que se hace es con la ecuacion de y'= .... se iguala a 0 hay 3 raices por que es un polinomio de grado 3, 2 de ellas estaran fuera del intervalo , esto interesa por que como queremos saber cual es la flecha maxima en el punto que y'0 sera la flecha maxima 

ymax = y(x=2) = -50*4^4/384 ei % iMPORTANTE VER LAS UNIDADES las cargas eran kn/m por lo que EI debe estar en kn y m lo normal es que de la E en gpa o en N/mm^4 y que la I calculada sea en mm^4 o cm^4 
el resultado final aqui es -3.3*10^-4 m es decir 0.3mm 

importante en la verificacion como ha tenido flexion hacia abajo tiene que ser  un valor negativo, no tendria sentido otra cosa, el diagrama de giros  tambien tiene sentido la explicacion es que la seccion inicial ha girado -26.6 es decir horario y en el otro 26.6 es deir antihorario positivo como se podia intuir en el dibujo y la seccion centrar  no ha girado nada sigue vertical

ejercicio con voladizo

empotramiento izquierda longitud de la barra 4m carga en x=4 10kn hacia abajo, en x= 0 carga puntual x= 10 hacia arriba y momento antihorario de 40knm 

1) ecuacion momentos flectores 
mf= 10x-40
2) EDE 
inty''dx = M/EI = int(10x-40/EI)dx
theta = y' = 1/ei = (10X^2/2 -40X +C1)
3) Y = Y'DX = 1/EI ( 5x^3/3 - 40x^2/2 + c1x +c2)
4) condiciones de contorno
y(x=0)= 0 
y'(x=0) =0 % como hay un empotramiento el giro esta restringido y por tanto es 0 en el inicio 
y(x=0)= 0 1/EI ( 5*0^3/3 - 40*0^2/2 + c1*0 +c2) ---> c2= 0
y'(5*0^2 -40*0 +C1) = 0 ---> c1 = 0 

flecha en x= 0  c2/EI
giro en x= 0 c1/EI 

si tenemos un empotramiento podemos sabeer que en el c1 y c2 = 0 con los apoyos se saca que y=0 = 0 c2 =0 

en los extremos y' = 0 , -80/EI % el primero para 0 el segundo para cuatro
en y'' 0, -213/EI % el primero para 0 el segundo para cuatro
representando Q MF y' que es thetha y y 
para representar el angulo de giro nos vamos al diagrama de Q como es constante y positivo nos dice que la segunda derivada de theta es positiva es decir que su curvatura es concava 
para dibujar la y nos fijamos en mf que son todo valores negativos por lo que su curvatura es negativa es decir convexa 
%el valor maximo sera -213/EI que tiene sentido por que el punto de theta = 0 es un maximo 
% otros ejemplos de condiciones de contono 1 apoyo fijo izquierda x=2 y otro en el empotramiento x= 5
% otro ejemplo 1 apoyo fijo en x=1 y otro movil en x=3 

en hiperestatica imaginando empotramiento izquierda y apoyo fijo un punto medio se hace por vanos calculando flecha maxima en cada tramo 

otro ejercicio 
carga triangular 30kn/m extremo izquierda apoyo fijo derecha movil  distancia entre ambos puntos 5m

1) calculo de reacciones y momentos 
 reaccion de 25 en izquierda derecha 50 momento flector 25x-x^3
2) EDE 
int y''dx = MF/EI = int 1/EI (25x-x^3)dx
theta = y' = 1/EI (25X^2/2 - x^4/4 +c1) 
y = 1/EI (25X^3/6 - x^5/20 +c1x +c2)
3) condiciones de contorno 
y(0) =0  
y = 1/EI (25*0^3/6 - 0^5/20 +c1*0 +c2) = 0 ---> c2 = 0
y(x=5)= 0 
y = y = 1/EI (25*5^3/6 - 5^5/20 +c1*5 +c2) ---> c1 = -875/12

dando valores en y'(0) = -72.9/EI y'(5) = 83.3/EI
y(0)=0 y(5) =0

dibujamos Q MF theta e y 
para Q pasan de 25 a -50 para los momentos flectores  de haber igualado Q = 0 ( se obtiene x= 2.88) % seguramente se haya necesitado para la resistencia en el Estado limite de la resistencia que es donde este el momento maximo 

dibujando la y' que parte de -72.9 /EI y acaba 83.3/EI fijandonos en la curva de cortantes, desde 0 a 2.88 hay una curvatura positiva  y luego es convexa, si igualamos y' en 2.88  vemos como se dibuja 
para la y con la ley de momentos flectores como son todo positivos la curvatura es siempre positiva 
calculando el y'=0 (que da 2.598) sabemos cual es la y max   que si hacemos y (2.598) nos sale -122/EI 


% puede ser que nos diga que el giro sea 0 en un punto si no lo podemos dibujar por que sea un polinomio >4 

problema apoyo fijo en ambos extremos en x=2 carga puntual de 10 hacia abjo distancia hasta el siguiente apoyo 3m 
cortes en ambos lados y se tiene 2 leyes de momentos , hay que poner una ecuacion diferencial para cada tramo
y'' = M/EI integramos para y' y otra vez para y que seran ambas validas solo para entre 0 y 2 que dara una c1 y c2 y luego hacer lo mismo que sera solo valido para x € 2,5 pero tendremos c3 y c4 

condiciones de contorno y(0=0) y(5=0) tambien sabemos que lo que pasa en para el tramo de la izquierda pasa tambien el de la derecha por tanto y(2) e y'(2) de ambas son igualas 

si tenemos una carga distribuida y varias cargas, no es operativo no lo haremos lo maximo es con 2 cortes