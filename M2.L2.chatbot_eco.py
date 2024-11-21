import random
import discord
from discord.ext import commands 

permisos = discord.Intents.default()
permisos.message_content = True

ecoh = commands.Bot(command_prefix = "=", intents = permisos)

@ecoh.event
async def on_ready():
    print(f"¡{ecoh.user} está en línea!")

@ecoh.command()
async def info(ctx):
    lista_comandos = ["*descompose* sirve para conocer el tiempo de descomposición de un objeto",
                      "*recycle* sirve para saber si el objeto se puede reciclar o no",
                      "*consejo* te daré un consejo que te puede ayudar a que tu día sea más ecológico (solo coloca =consejo)"]
    
    await ctx.send("¡Hola! 👋 soy Ecoh, para activar una de mis funciones coloca = y el nombre del comando junto al objeto sobre el que se va a aplicar el comando")
    await ctx.send("A continuación te voy a mostrar los comandos que utilizo:")
    await ctx.send(lista_comandos)

@ecoh.command()
async def descompose(ctx,*,objeto:str):
    listaDescomposition = {
        "botella de plástico": 500,
        "chicle": 10,
        "vidrio": 5000
    }
    
    objeto = objeto.lower()

    if objeto in listaDescomposition:
        await ctx.send(f"El {objeto} tarda en descomponerse aproximadamente {listaDescomposition[objeto]} años")
    else:
        await ctx.send(f"No tengo información al respecto")

@ecoh.command()
async def recycle(ctx, *, thing:str):
    lista_Reciclables = ["revistas", "revista", "periódico", "periódicos",
        "cajas", "caja de cartón", "cuaderno", "cuadernos", "botella de vidrio",
        "botella de plástico", "coca cola", "tapa", "tapas", "funda", "envase de madera",
        "madera", "latas", "muebles", "refrigeradora", "microondas", "cocina", "lavadora",
        "foco", "focos", "cassettes", "papel", "cartón", "vidrio", "pila", "pilas", "baterías",
        "tela"]

    lista_noReciclables = [
        "funda de basura", "juguetes", "pasta dental", "esferos", "chicles", "encendedor", "pastillas",
        "aerosol", "pintura", "pesticida", "insecticida", "platos", "toallas", "servilletas" 
    ]

    thing = thing.lower()

    if thing in lista_Reciclables:
        await ctx.send(f"Sí lo puedes reciclar 🥳")
    
    elif thing in lista_noReciclables:
        await ctx.send(f"No lo puedes reciclar, deséchalo a la basura 😊")
    
    else:
        await ctx.send(f"No tengo información al respecto 😞")


@ecoh.command()
async def consejo(ctx):
    lista_consejos = [
        "¡Clasifica tus residuos y lleva a cabo el reciclaje!",
        "Hoy opta por bolsas reutilizables y evita productos desechables",
        "Toma una ducha más corta y cierra el grifo mientras te cepillas los dientes",
        "Desenchufa los electrodomésticos cuando no los estés utilizando",
        "¡Hoy transpórate en bicicleta!, verás lo divertido que es"
    ]
    
    consejo = random.choice(lista_consejos)
    await ctx.send(f"{consejo}")
