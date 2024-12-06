stands = {
            "Star Platinum": "Stand Humanoide, espesializado en combate cuerpo a cuerpo, con un rango de 5 metros, con el poder de The World, que le permite parar el timepo. Usuario: Jotaro Kujo, estado actual: Fallecido" ,
            "Tusk: Act 4": "Stand de rango medio-largo. Esta especializado en el spin, poder que le permite hacer rotar objetos, crear agujeros de gusano donde solo el usuario puede estar, hacer que objetos roten infinitamente, y atravezar cualquier barrera. Usuario: Jhonny Joestar, estado actual: Fallecido",
            "Wonder of U": "Stand de rango corto, con el poder de brindar la calamidad a cualquier persona que lo busque a el o a su usuario, transformando a todo el mundo en un arma mortal. Usuario: Ninguno, estado actual: fallecido",
            "Killer Queen: Bites the dust": "Tiene el poder de crear explosiones a voluntad, tiene 3 habilidades: Volver cualquier objeto que toque una bomba, crear una mina andante que persigue a la fuente de calor más cercana, y Bites the Dust, que le permite adjuntar a Killer Queen a cualquier persona, y si alguien descubre la identidad del usuario, causa que el día se reinicie, haciendo que cualquier cambio sea permanente. Usuario: Joshikague Kira, estado actual: Fallecido"
            }

word = input("Escribe un stand de Jojo's (Solo de material canon): ")

if word in stands.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(stands[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Ese stand no esta en mi base de datos actual")
