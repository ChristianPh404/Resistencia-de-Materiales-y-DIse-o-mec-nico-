en la pagina 234 meter estas aclaraciones
entre b y c hay flexion pura por que Q= 0 N=0 y si hay flexion
la deformacion se mide con epsion y gamma 
si las secciones tiene angulos rectos despues de deformarse se mantienen los angulos rectos
no hay distorsion 




en la 235 
sometida a momento flector positivo , abajo de todo se alarga arriba se acorta y en el medio
fibra neutra que ni se alarga ni se acorta deformacion unitaria = 0 y por tanto la tension 0 

desde fibra neutra y positiva hacia arriba y negativa hacia abajo 

dibujamos un rectangulo que seria una de las secciones con base dx (en vertical) tras deformarse se hace una epecie de cono  f es el radio de curvatura de la fibra neutra , es decir buscando el centro desde donde dibujariamos los arcos es decir desde el punto O hasta donde estaria la fibra neutra en un extremo (para el otro seria igual)  a una distancia y 
para arriba positiva abajo negativa, en un punto superior es decir Y > 0 tomamos dos puntos N el de antes de la deformacion y M el de despues, si hacemos semejanza de triangulos A B O  es semejante al BNM al tener ambos un angulo recto y la recta OB esla que pertenece tambien a MB , AB/OA = MN/NB  es decir dx/2 /rho (rho es el radio de curvatura de la fibra neutra) = -incremento de diferencial de x/2 (es un acortamiento asi que tiene que ser negativo) / y (ademas es /2 el incremento debido a que existen dos triangulos y trabajamos solo con uno)

ydx = -delta dx rho 
delta dx/dx = - y /rho
epsion_nx = sigma_nx/E = - y/rho
sigma_nx = -rho y /rho 

en la diapositiva 7 (de "Tema Flexión tensiones cma.pdf", correspondiente a la deducción N=0): al imponer flexión pura (N = 0), N = integral sigma_x dA = integral (-E*y/rho) dA = 0. Como el módulo elástico E y el radio de curvatura rho son constantes en la sección, salen fuera de la integral: (-E/rho) * integral y dA = 0 => integral y dA = Sy = 0 (el momento estático respecto al eje neutro es nulo). Por la definición y propiedades del momento estático, esto demuestra directamente que el eje neutro (fibra neutra) contiene al centro de gravedad (pasa por el centroide de la sección).

*(Nota: en la diapositiva 17 de dicha presentación se expone la Hipótesis generalizada de Navier-Bernoulli para flexión simple: las secciones experimentan alabeo por cortante, pero si Q=cte o aproximadamente cte, el alabeo es cte y se puede seguir aplicando la fórmula de Navier para tensiones normales).*

con la formula de navier si se puede calcular la tension y la k para calcular las deformaciones, la curvatura K se define como la inversa del radio de curvatura

las tensiones maximas se dan en los extremos puesto que depende la tension dependera de Y el resto sera constante (aclarar en la figura 5.6) en el eje neutro tendra tension 0

imaginando que tenemos un prisma y queremos saber la distribucion de tensiones en la seccion ( se podria tener o a lo largo de la pieza o dentro de la seccion dando un corte vertical) la vista desde la derecha seria rectangular con el centro de gravedad en su centro, la x coincidira con el centro que sera la fibra neutra (realmente hay muchas todas las que pasen por el centro) habra un momento flector positivo  saldria una tension negativa al ser y positiva I siempre es positiva , saliendo una tension negativa que tiene sentido por que seria compresion

por convenio se representar las tensiones positivas a la derehca y en el ej x la escala de las tensiones 

perfiles tipicos de acero
doble T, C (se dicen en U ) en L  estan estandarizadas y hay tablas  con sus dimensiones  IPN IPE HEI  , donde vienen tabuladas h b A Iy Iz sx s W 

cuando queramos dimensionar una pieza momento maximo * y max / I si estamos en un problema de dimensionamiento y no de comrpobacion ymax es una incognita y sera la pregunta ademas tampoco conoceremos su inercia ya que depende de la geometria de la pieza

lo que se hace es que se engloba ambas variables I e y en una ya que estan en las tablas I/ymax = W que es el modulo resistente , imponiendo esta condicion se puede despejar
en la formula sigma = M y /I me interesa que las tensiones sea lo menor posible por lo que tengo que buscar una geometria que minimize las tensiones en traccion lo conseguia aumentando el area, en flexion aumentando la ineria ( no basta que la pieza sea mas grande hay un ejercicio con 3 secciones y las 3 tienen la misma area pero diferente geometria una es una especie de + otra es un rectangulo vertical y otra I las 3 tienen la misma altura es decir ymax  omega1=omega2=omega3 pero las inercias seran diferente) si no cumplen los perfiles se refuerzan poniendo placas de acero en los extremos 
ejercicio de aplicacion de la formula 

una especie de TT donde hay 160 de horizontal las cotas en horizontal son 40 20 40 20 40 donde los 20 son los grosoreslas partes verticales y 40 la de horizontal altura de la pieza 80, 60 seran la parte vertical y 20 el grosor

Pide distribucion de tensiones en la seccion 
para Md = -300kn 
Md = 200knm
Comprobar resistencia a ELU
fkt = 3.3n/mm^2 gamma = 1.1 (gamma es el coeficiente de minoracion)
fkc = 11 n/mm^2
maximo momento que puede soportar 

Izg = 3020952.43 cm^4 

52,86 es yG por lo que se divide la pieza en 27.14 arriba y 52.86 abajo 
para el momento de -300
sigma para 27.14= -(-300*10^6)*(271.4) /3020952.43 = 2.69N/mm^2
sigma para y = -52.86 = -(-300*10^6)*-(528.6) /3020952.43 = 2.69N/mm^2 

para el momento de 200 

sigma para 27.14= -(-200*10^6)*(271.4) /3020952.43 = 1.79N/mm^2
sigma para y = -52.86 = -(-300*10^6)*-(528.6) /3020952.43 = 2.69N/mm^2 

ahora comprobar resistencia con los valores admisibles como me daban los momentos mayorados las tensiones ya son mayoradas, tension maxima mayorada <= tension admisible max
traccion 2.69 y 3.5 tension admisible maxima era 3.3/1.1 por tanto solo cumple para uno de los dos momentos la de compresion que es 11/1.1  , el valor de compresion era 5.25 y 1.9 , es decir la pieza aguanta ambos de compresion pero de trccion para la tension de 3.5 no cumple 

maximo momento positivo que puede aguantar la pieza: compresiones arriba tracciones abajo , incognita ahora seria M imponiendo ambos limites tmax de compresion <= tadm compresion y tmax tra <= tadm traccion 
Md = 1113*10^6 Nmm arriba
Md = 171.5*10^6 Nmm abajo 

con el vector tension que tiene una componente normal y tangencial nos interesa la tangencial para el cortante en la flexion simple como las tensiones estan contenidas en la seccion se representan como en la figura 5.7 si en un lado tienes cortante Q por ejemplo 8 en el otro no tiene por que ser lo mismo, cortante para abajo tensiones para abajo cortante para arriba tension para arriba , 
las tensiones tangenciales se calculan con la formula de (principio de reprocidad de las tensiones tangenciales) las tensiones en dos aristas del solido son convergentes o divergentes 

** Importante en los examenes siempre se pregunta el calculo de las tensiones tangenciales**
Como se haria si me preguntasen calcula la tension tangencial en la linea  a una distancia y = 10 de la pieza anterior, sobre el centro de gravedad

tau(y= 10) = 20*S/b(y)* I  ( b es 160 en ese caso) 
( S*(y=10)) = omega* * ygc  es decir el area es desde donde yo quiero calcular hacia fuera es decir 160*17.14 // repasar el 17.14 que es dudoso 
luego buscar el centro de gravedad y la y de su centro de gravedad

la tension tangencial maxima sera maxima en el centro de gravedad para las piezas que trabajaremo que seran o rectangulares o I o T 

---

## Ejercicios Adicionales Resueltos (Tema 5: Flexión Pura y Simple)

### Ejercicio 1: Cálculo de distribución de tensiones tangenciales en viga armada
*(Procedencia: `inercia/CALCULO TENSIONES TANGENCIALES.pdf`)*

**Enunciado:**
Calcular la distribución de tensiones tangenciales para un esfuerzo cortante de cálculo $Q_d = 95\text{ kN}$ en la viga armada de acero S275 cuya sección es un perfil doble T asimétrico con las siguientes dimensiones:
- **Ala superior:** anchura $b_1 = 400\text{ mm}$, espesor $t_1 = 8\text{ mm}$.
- **Alma:** altura $h_w = 300\text{ mm}$, espesor $t_w = 6\text{ mm}$.
- **Ala inferior:** anchura $b_2 = 200\text{ mm}$, espesor $t_2 = 8\text{ mm}$.
- Altura total: $H = 8 + 300 + 8 = 316\text{ mm}$.

**Resultados y pasos clave:**
1. **Posición del centro de gravedad ($y_G$ medido desde la base inferior):**
   - $A_{\text{total}} = (400 \cdot 8) + (300 \cdot 6) + (200 \cdot 8) = 3200 + 1800 + 1600 = 6600\text{ mm}^2$.
   - $y_{cdg} = 195.33\text{ mm}$ (desde el borde inferior).
   - Distancia del c.d.g. al borde superior: $316 - 195.33 = 120.67\text{ mm}$.
2. **Momento de Inercia respecto al eje neutro ($I_{zG}$):**
   - Calculado por Steiner para cada uno de los 3 rectángulos respecto al eje baricéntrico.
3. **Distribución de tensiones tangenciales $\tau(y) = \frac{Q_d \cdot S^*(y)}{b(y) \cdot I_{zG}}$:**
   - **En el extremo superior ($y = +120.67\text{ mm}$):** $\tau = 0\text{ N/mm}^2$.
   - **En la unión ala superior / alma ($y = 120.67 - 8 = +112.67\text{ mm}$):**
     - En el ala ($b = 400\text{ mm}$): $\tau = 0.75\text{ N/mm}^2$.
     - En el alma ($b = 6\text{ mm}$): salto brusco por reducción de anchura:
       $$\tau = 0.75 \cdot \frac{400}{6} \approx 50.03\text{ N/mm}^2$$
   - **En la fibra neutra (Centro de Gravedad, $y = 0$):**
     - Máximo absoluto de la sección:
       $$\tau_{\max} = 55.13\text{ N/mm}^2$$
   - **En la unión ala inferior / alma ($y = -187.33\text{ mm}$):**
     - En el alma ($b = 6\text{ mm}$): $\tau = 41.02\text{ N/mm}^2$.
     - En el ala inferior ($b = 200\text{ mm}$): $\tau = 1.23\text{ N/mm}^2$.
   - **En el extremo inferior ($y = -195.33\text{ mm}$):** $\tau = 0\text{ N/mm}^2$.

---

### Ejercicio 2: Flexión Pura y Comprobación ELU / Momentos Máximos Admisibles
*(Procedencia: `inercia/EJERCICO CALCULO MOM MAX Q AGUANTA.pdf`)*

**Enunciado:**
Dada una sección transversal en forma de doble T invertida / perfil "TT" con:
- Ala superior de anchura $160\text{ cm}$ y espesor $20\text{ cm}$.
- Dos almas verticales de espesor $20\text{ cm}$ cada una y altura $60\text{ cm}$, separadas $40\text{ cm}$ entre sí y con voladizos de $40\text{ cm}$.
- Altura total $80\text{ cm}$.
- Material: $f_{ctk} = 3.3\text{ N/mm}^2$ (resistencia característica a tracción), $f_{ck} = 11\text{ N/mm}^2$ (resistencia característica a compresión).
- Coeficientes de seguridad: $\gamma_s = 1.1$ (minoración del material), $\gamma_f = 1.5$ (mayoración de acciones).
  - Tensiones admisibles de cálculo:
    $$\sigma_{adm, T} = \frac{3.3}{1.1} = 3.0\text{ N/mm}^2, \quad \sigma_{adm, C} = \frac{11}{1.1} = 10.0\text{ N/mm}^2$$

**Cálculos geométricos:**
- Posición del centro de gravedad: $y_G = 52.86\text{ cm}$ desde la base inferior.
  - Distancia a la fibra superior: $y_{\sup} = +27.14\text{ cm} = +271.4\text{ mm}$.
  - Distancia a la fibra inferior: $y_{\inf} = -52.86\text{ cm} = -528.6\text{ mm}$.
- Momento de inercia baricéntrico:
  $$I_{zG} = 3020952.43\text{ cm}^4 = 3.020952 \times 10^{10}\text{ mm}^4$$

**Apartados:**
- **a) Distribución para $M_d = -300\text{ kNm} = -300 \times 10^6\text{ N}\cdot\text{mm}$ (momento negativo: tracción arriba, compresión abajo):**
  - $\sigma_{\sup} = -\frac{(-300 \times 10^6) \cdot (+271.4)}{3.020952 \times 10^{10}} = +2.69\text{ N/mm}^2 \le 3.0\text{ N/mm}^2$ (Cumple a tracción).
  - $\sigma_{\inf} = -\frac{(-300 \times 10^6) \cdot (-528.6)}{3.020952 \times 10^{10}} = -5.25\text{ N/mm}^2 \implies |\sigma_{\inf}| = 5.25 \le 10.0\text{ N/mm}^2$ (Cumple a compresión).
  - **Resultado:** **Resiste** a ELU.
- **b) Distribución para $M_d = +200\text{ kNm} = +200 \times 10^6\text{ N}\cdot\text{mm}$ (momento positivo: compresión arriba, tracción abajo):**
  - $\sigma_{\sup} = -\frac{200 \times 10^6 \cdot (+271.4)}{3.020952 \times 10^{10}} = -1.80\text{ N/mm}^2 \implies 1.80 \le 10.0\text{ N/mm}^2$ (Cumple a compresión).
  - $\sigma_{\inf} = -\frac{200 \times 10^6 \cdot (-528.6)}{3.020952 \times 10^{10}} = +3.50\text{ N/mm}^2 > 3.0\text{ N/mm}^2$ (**NO CUMPLE** a tracción).
  - **Resultado:** **No resiste**. Empezaría a romper por tracción en la fibra inferior.
- **c) Momentos máximos que puede aguantar:**
  - **Momento positivo máximo ($M_{d}^+$):**
    - Por compresión superior: $M_d \le \frac{10 \cdot I}{271.4} = 1113 \times 10^6\text{ N}\cdot\text{mm}$.
    - Por tracción inferior: $M_d \le \frac{3 \cdot I}{528.6} = 171.5 \times 10^6\text{ N}\cdot\text{mm}$.
    - El más restrictivo de cálculo es $M_d^+ = 171.5\text{ kNm}$.
    - Momento característico aplicable: $M_k^+ = \frac{171.5}{1.5} \approx 114.3\text{ kNm}$.
  - **Momento negativo máximo ($M_{d}^-$):**
    - Por tracción superior: $|M_d| \le \frac{3 \cdot I}{271.4} = 333.9 \times 10^6\text{ N}\cdot\text{mm}$.
    - Por compresión inferior: $|M_d| \le \frac{10 \cdot I}{528.6} = 571.5 \times 10^6\text{ N}\cdot\text{mm}$.
    - El más restrictivo de cálculo es $|M_d^-| = 333.9\text{ kNm}$.
    - Momento característico aplicable: $M_k^- = \frac{333.9}{1.5} \approx 222.6\text{ kNm}$.

---

### Ejercicio 3: Determinación de la máxima carga repartida admisible $q$
*(Procedencia: ejercicio del examen / foto adjunta)*

**Enunciado:**
Determinar la máxima carga repartida uniforme $q$ ($\text{kN/m}$) que puede soportar una viga continua con voladizo si la tensión admisible del material es $\sigma_{\text{adm}} = 262\text{ N/mm}^2$.
- **Geometría y cargas:**
  - Tramo $A-B$: $L_1 = 4\text{ m}$. Tramo en voladizo $B-C$: $L_2 = 2\text{ m}$.
  - Carga uniforme $q$ actuando en toda la longitud ($6\text{ m}$).
  - Momento puntual horario aplicado en $A$: $M_A = 10\text{ kNm}$.
  - Momento puntual horario aplicado en $B$: $M_B = 10\text{ kNm}$.
- **Sección transversal (perfil I simétrico):**
  - Anchura de alas: $b = 60\text{ mm}$, espesor $t_f = 10\text{ mm}$.
  - Alma central: altura libre $h_w = 200\text{ mm}$, espesor $t_w = 10\text{ mm}$.
  - Altura total $H = 220\text{ mm}$, $y_{\max} = 110\text{ mm}$.
- **Diagramas de esfuerzos y momentos críticos:**
  - En el vano interior ($A-B$): $M(x) = 10 + 1.125\,q$ (en el punto de cortante nulo $x = 1.5\text{ m}$).
  - En el apoyo $B$ (voladizo): momento negativo $|M| = 2\,q$.
  - Condición de diseño por flexión: $\sigma_{\max} = \frac{|M_{\max}| \cdot y_{\max}}{I_z} \le \sigma_{\text{adm}}$.
- **Solución:**
  - Comparando los posibles puntos críticos frente al límite elástico, el momento global determinante da como resultado:
    $$q_k = 15.8\text{ kN/m} \quad (\text{o } 19.21\text{ kN/m según criterio de combinación considerado})$$ 