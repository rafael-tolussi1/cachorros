import discord
from discord.ext import commands
from comandos import get_class
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def image(ctx):
    imagens = ctx.message.attachments
    for imagem in imagens:
        nome = imagem.filename

        await imagem.save(f"imagens/{nome}")

        classe = get_class(model = "keras_model.h5", label = "labels.txt", image = f"imagens/{nome}")

        if classe == "Buldogue Francês":
            await ctx.send("Buldogue Francês_Pequeno, carinhoso e muito divertido.")
        elif classe == "Dogue Alemão":
            await ctx.send("Dogue Alemão_Gigante, elegante e gentil")
        elif classe == "Golden Retriever":
            await ctx.send("Golden Retriever_Amigável, inteligente e brincalhão.")
        elif classe == "Husky Siberiano":
            await ctx.send("Husky Siberiano_Energético, resistente e aventureiro.")
        elif classe == "Pitbull":
            await ctx.send("Pitbull_Forte, leal e cheio de energia.")

bot.run("TOKEN")