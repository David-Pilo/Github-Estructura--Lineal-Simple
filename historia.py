import time
def continuar():
   input("\nPresiona Enter para continuar...")

nombre = input("Introduzca su nombre: ")
edad = input("Introduzca su edad: ")
residencia = input("Introduzca su ciudad residencia: ")

print (f"Hola mi nombre es {nombre} tengo {edad} años y soy de {residencia}")
continuar()

#Preguntas
ocupacion = input("¿A qué te dedicas?: ")
estudios = input ("¿Qué estudias?")
hobby = input("¿Cuál es tu pasatiempo favorito?: ")
sueño = input("¿Cuál es tu mayor sueño?: ")
mascotas = input("¿Tienes mascotas, como se llaman?: ")
mejor_amigo = input("¿Como se llama tu mejor amigo?: ")
sueño_pequeño = input("¿Que querias ser de pequeño?: ")
if len(sueño_pequeño) > 0 and sueño_pequeño[-1] in "aeiouAEIOU":
    sueño_plural = sueño_pequeño + "s"
else:
    sueño_plural = sueño_pequeño + "es"

escuela_primaria = input("¿A que Escuela primaria fuiste?: ")
lugar_de_nacimiento = input("¿en que pais nacistes? " )
estado = input("¿eres solter@ o casad@?")
comida_favorita = input("¿cual es tu comida favorita?")




print("\n--- Historia del protagonista ---")
time.sleep(1)

print(f"{nombre} vive en {residencia} y tiene {edad} años.")
print(f"Actualmente se dedica de {ocupacion}.")
print(f"En su tiempo libre le gusta {hobby}.")
print(f"Su mayor sueño es {sueño}.")
print(f"Esta es solo una parte de la historia de {nombre}, que apenas comienza.")
time.sleep(1)
print(f"Cuando era pequeño soñaba con ser {sueño_pequeño}")
print(f"Se imaginaba que era {sueño_pequeño} y eso lo hacía muy feliz.")
print(f"Junto a su mejor amigo {mejor_amigo} pasaban horas jugando que eran {sueño_plural}")
print(f"A medida que pasaron los años, cuando se encontraba en la escuela de {escuela_primaria},")
print(f"Se dio cuenta de que su verdadera vocación era {sueño} y eso lo cambió todo. ")


# Aporte al desarrollo de la historia
color_favorito = input("¿Cuál es tu color favorito?: ")
musica_favorita = input("¿Cuál es tu musica favorita?: ")
momento_feliz = input("Cuéntanos un recuerdo o momento que te haga feliz: ")

print(f"\nCaminar por las calles de {residencia} siempre le trae recuerdos a {nombre}.")
print(f"A veces, mientras escucha su música favorita, que es {musica_favorita},")
print(f"se detiene a pensar en {momento_feliz}, un momento que lleva grabado en el corazón.")
print(f"Curiosamente, siempre que ve el color {color_favorito}, {nombre} recuerda que")
print(f"la vida está llena de detalles que hacen que estudiar {estudios} valga la pena.")
continuar()


print(f"Capitulo 2: La meta de {nombre}")
time.sleep(1)

meta_futura = input("¿Qué meta quieres cumplir en los próximos años?: ")
lugar_viajar = input("¿A qué país o ciudad te gustaría viajar algún día?: ")
persona_inspiracion = input("¿Qué persona te inspira en la vida?: ")
miedo = input("¿Cuál es uno de tus mayores miedos?: ")

print(f"\nCon el paso del tiempo, {nombre} comenzó a pensar más en su futuro.")
print(f"Sabía que quería lograr algo importante: {meta_futura}.")
print(f"Aunque a veces sentía miedo, especialmente a {miedo},")
print(f"recordaba las palabras de {persona_inspiracion}, quien siempre fue una gran inspiración.")
time.sleep(2)

print(f"{nombre} soñaba también con viajar a {lugar_viajar},")
print(f"conocer nuevas culturas y aprender cosas que le ayudarían a crecer como persona.")
continuar()


print(f"\nCapitulo 3: Nuevos caminos")
time.sleep(1)

valor = input("¿Qué valor consideras más importante en la vida?: ")
reto = input("¿Cuál ha sido uno de los retos más grandes que has superado?: ")
lugar_feliz = input("¿Cuál es un lugar donde te sientes completamente feliz?: ")

print(f"\nA lo largo de su vida, {nombre} aprendió que el valor de {valor} era fundamental.")
print(f"Recordaba cuando tuvo que enfrentar {reto}, una experiencia que lo hizo más fuerte.")
print(f"Cada vez que las cosas se complicaban, pensaba en {lugar_feliz},")
print(f"un lugar donde siempre encontraba tranquilidad y motivación para seguir adelante.")
continuar()


print(f"\nCapitulo Final: El futuro de {nombre}")
time.sleep(1)

mensaje_final = input("Escribe un mensaje que te gustaría decirle a tu yo del futuro: ")

print(f"\nHoy, {nombre}, con {edad} años, vive en {residencia} y sigue construyendo su historia.")
print(f"Sus sueños, como convertirse en {sueño}, siguen guiando cada paso que da.")
print(f"Junto a amigos como {mejor_amigo} y los recuerdos de su infancia,")
print(f"sabe que cada experiencia lo ha llevado hasta donde está hoy.")

print(f"\nAntes de continuar su camino, {nombre} deja un mensaje para el futuro:")
print(f"\"{mensaje_final}\"")

time.sleep(2)

print("\n--- FIN DE LA HISTORIA ---")
print(f"La historia de {nombre} continúa... porque cada día es una nueva aventura.")
