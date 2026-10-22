parecido a problema 9 la figura fuerza de compresion 1m del tope 200kn hacia arriba 100 hacia abajo (en el extremo) altura del cuerpo inferior 1m de los superiores 3m  50kn/m de fuerza hacia abajo simbolo de seccion rectangular 10cm^2 y abajo 15cm^2 
representar ley de axiles y tensiones sin tener en cuenta el peso propio

primero trasladarlo a horizontal es decir empotramiento izquierda
3 cortes 0 a 1 1 a 3 y de 3 a 4

el diagrama de tensiones es dividir el de esfuerzos axiles al de tension 

no en todos los problemas es necesario realizar todos los cortes depende de la geometria como solo queremos el diagrama de axiles si nos quedamos con la parte derecha en este caso no hay que calcular reacciones

Ni= 3 
NE= 3 ---> isoestatica
summH =0 = Ha-50 +200 - 100 -50*3 \\ ha =100  los -50*3 es por que la carga era distribuida
summFv = 0 = VA
summM= 0 = MA

seccion1 
summfh = 0 = 100+N --> N= -100kn

segunda seccion x 1-3
summfh= 0 = 100-50-50(x-1) --> N= 50x - 100

n1 = -50kn 
n3= 50 kn

seccion 3 , quedandonos con la parte de la derecha
summfh = -N - 100 -50*(4-x) --> N = 50x - 300

Representando diagrama de axiles

1) Seccion 1 de 0 a 1 compresion
    N(0) = -100
    N(1) = -50
2) Seccion 2 de 1 a 3 empieza en compresion y termina en traccion
    N(1) = -50
    N(3) = 50
3) Seccion 3 de 3 a 4 compresion
    N(3) = 50
    N(4) = 50*4 - 300 = -100
Diagrama de tensiones = axiles/area en N/mm^2

-66.67N/mm^2  linea recta const hasta x=1 \\ hay que dividir 50000/1000 que son -50 ya que se divide el salto de -50 por la seccion de 10
luego 50 entre el area que vuelve a quedar positivo y posteriormente el nuevo N/area = -100 N/mm^2

la pregunta tipica seria si resiste el material, para ello se usa el maximo y se compara, tambien hay casos como el acero que tiene la misma resistencia caracteristica a traccion que a compresion si resiste la pieza y es de acero, lo que se hace es buscar cual es la tension maxima en valor absoluto y se compara con la admisible, si no es acero y es otro material, se tiene que hacer lo siguiente por una parte buscar donde se da la tension maxima a compresion y se compara con la admisible del material (en valor absoluto) ej los 150  aqui
luego lo mismo pero con traccion que serian los 50  tambien se puede calcular alargamiento, se calcula el incremento de longitud usando int N/ E omega dx 

la integral hay que dividirla en tantos intervalos como cambios haya de E y omega de 0 a 1 hay un axil por lo que sera uno de los tramos con axil 0 -100 E del material y la omega que eran 15 + la integral entre 1 y 3 del axil (-100+50x )/ (E omega) +  int entre 3 y 4 axil (50x-300)/(E omega)

\IMP el diagrama de axiles es independiente de las secciones del material solo depende de las cargas pero en el de alargamiento si que importa si hubiera cambiado la seccion en 1.5 el cambio hubiera sido añadir + int 1 a 1.5 del axil (-100*50x)/(E*15) y luego cambiaria la integral que seguia que ahora iriaa de 1.5 a 3 

\section{Pilar de seccion 0.25*0.25 carga en su eje de 40kn , altura 5m y teniendo en cuenta el peso propio sabiendo que es 20kn/m3 E=700n/mm2}

Piden acortamiento/alargamiento del pilar 

Para aplicar la formula anterior necesitamos calcular la ley de axiles

como el peso abajo acumula todo lo que lleva arriba la carga se comporta como una uniformemente repartida al multiplicar la seccion por el peso especifico 20kn*0.25*0.25 = 1.25 kn/m 

para calcular el diagrama de axiles, no hace falta calcular las reacciones en este caso pero sirve de comprobracion para ver que el diagrama de axiles esta bien, trasladamos el diagrama para tener el DCL en horizontal
summfh = 0 = HA -1.25x -40 --> HA = 46.5kn (x=5)
MA = 0 =VA 

ley de axiles summfh = 0 = 46.5 -1.25x +N --> N= -46.5 +1.25x
N(0) = -46.5 kn
N(5) = -46.5 +1.25*5 = -46.5+6.25 = -40.25 kn
al representarlo todo compresion que va lineal de -46.5 a -40.25

calcular alargamiento

incremento de longitud AB= int_XA^XB (1.25x-46.5/700*10^3 * 0.25*0.25)dx \\ pasando los 700N/mm^2 a kn/m^2 A = 0 B =5

= 1/43.750*(1.25x^2/2 -46.5x) evaluado entre 0 y 5 = -4.99*10^-3 m


Apartado de teoria antes de los problemas traccion/compresion uniaxial hiperestatica

consiste que hay casos en los que no puede haber ni = ne , ya que ni> ne , añadiendo tantas ecuaciones como se necesiten para poder resolverlo es decir GH = 0 ejemplo NI=5 NE=3 GH=2 se añaden 2 ecuaciones de compatibilidad en deformaciones, son las que nos habilitan la resolucion 

Diferentes situaciones posibles 
1) hiperestaticidad por los materiales
2) hiperestaticidad por el tipo de apoyo 
3) hiperestaticidad por los tirantes

para el caso 1 
suponemos que hay una viga con 2 apoyos fijos en los extremos fuerza de compresion , pieza de longitud L fuerza f1 y f2 en extremos
lo primero seria calcular las reacciones (Ni = 4 ne= 3 GH = 1)
ecuaciones de equilibrio summfx = 0 = HA+HB+F1-F2
summfv = VA+vb
summMa = 0 VB*L 
la ecuacion adicional que se resuelve es decir la de compatibilidad 
como no se puede ni alargar ni acortar por los apoyos fijos 
incrmento de longitud A-B = 0 se mete la ecuacion de incremntoL _AB = int Na/ E omega dx 
N = f(HA,HB)

ejemplo en un rectangulo con la izquierda un apoyo fijo, a la derecha de este otro de grosor inferior acabando en un apoyo fijo en x=6 en el primero  hay una carga q=45kn/m se representa con flechas a la izquierda donde cada vez seran mas grande desde x=0 a x=3 que empieza en 0kn y acaba en 45knm y luego en la otra seccion va hacia la derecha de carga de 10kn al principio es decir x=3 y luego 15kn a x=4 primera seccion 200mm^2 segunda 100mm^2 E constante al ser mismo material 

primer paso resolucion del diagrama de axiles
posible pregunta la resistencia de la pieza donde se necesita como dato la tension admisible 

Primero las reacciones  summ fx =Ha + HB+10 + 15 - 45*3/2  
summ fv= 0 0 VA+VB
summ M =0 = vB*6 = 

ecuacion de incremento L --- > dibujando el triangulo seccion 1 x€ [0,3] y haciendo semejanza de triangulos 45/3 = q/x --> q=15x
summfx= 0 = HA+ N -15x *x/2 --> N = -HA +7.5x^2
SEGUNDO TRAMO X€ [3,4] 
summfh = 0 = HA+N+10 -45*3/2
N = 57.5-HA
Seccion 3  x€ [4,6] en este caso se puede hacer pero normalmente es mejor quedarse con el de la izquierda asi que se procede como en ese caso
summfh = 0 = HA+N+10+15-45*3/2 --> N=  42.5-HA

incremento de L = 0 = integral 0 a 3 (7.5x^2-HA)dx/(E*200*10E-6) + int 3 a 4 (57.5-HA)dx/(E*100*10E-6) + int 4 a 6 (42.5-HA)dx/(E*100*10E-6) 

sacamos de las integrales 1/E*100*10E-6
= 1/E*100*10E-6*( (0 a 3 1/2*(7.5x^3/3-HAx)evaluado entre 0 y 3+ ( (57.5x-HAx)entre 3 y 4  + (42.5x-HAx)entre 4 y 6) 

4.5HA = 176.5 ---> HA = 39.17 y se sustituye en la ecuacion de la lnea 101 y sale HB = 3.33kn
primer tramo
N = 7.5x^2 -HA 
N0 = -39.17
N3 = 28.33 
segundo tramo 
N= 57.5-HA
N3 = ne= 18.33
tERCER TRAMO
N = 42.5-HA
 n4= n6 = 3.33

 representacion del diagrama de axiles 

 Si la pregunta seria resiste la pieza, se calcula las tensiones, haciendo el diagrama de tensiones luego se busca la maxima de compresion y se compara con la admisibe y lo mismo para traccion 

  siguiente tipo de problema: caso de dos materiales unidos que se deforman solidariamente

  ejemplo un cilindro compuesto de 2 materiales dibujar en vertical, en la base se ve como una base cuadrada  y en el tope se ve que acaba en otra base cuadrada ,es decir como si tuviera placas en la base y en el tope, abajo esta empotrada y la de arriba para poder aplicarle una carga F de entrada y que se reparta bien, por fuera el cilindro tiene un material A mientras que por dentro tiene un material B , el material A tiene E_A y omega_A  sigma_admA, el B tiene E_b y omega_b y sigma_admB altura l , F es un dato conocido 
  Pregunta resiste la pieza? despreciar el peso propio 

es decir comparar tension maxima con la admisible de cada material, para calcular el axil como una parte de la carga ira al material A y otra al B se sabe que F = FA+FB y como no hay ninguna carga mas a lo largo de la pieza Fa= NA y FB = NB que ademas seran ambos constantes esto representa una situacion hiperestatica por que tiene una ecuacion con dos incognitas

por lo que es necesario una ecuacion de compatibilidad en deformaciones
como dice solidariamente ambos se deforman por igual y por tanto alargamiento de A = alargamiento de B 

 NA*L /EA*omegaA = NB*L/EB*omegaB --> NA*EB*omegaB = NB*EA*omegaA ( si en lugar de ser un tubo fuera un cono ya no seria eso)
 FA = FB*EA*omegaA/EB*omegaB de forma que FA = una constante* FB 
 y se sustituye en F = FA+FB y ya con eso si se puede calcular las tensiones y comparar las maximas con las admisibles 