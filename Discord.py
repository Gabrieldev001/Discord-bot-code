import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f"estou ligado como {bot.user}")

@bot.command(name="oi")
async def send_hello(ctx):
  resposta = f"ola {ctx.author}"
  await ctx.send(resposta)

@bot.command(name="menu")
async def what_me(ctx):
  cmd = f"menu para {ctx.author}"
  manusear = f"os comandos sao: !oi, !menu, !user, !desenhar, !caminhar"
  await ctx.send(cmd)
  await ctx.send(manusear)
@bot.command(name="user")
async def ho(ctx):
  quem = f"você é {ctx.author}"
  await ctx.send(quem)

@bot.command(name="desenhar")
async def desenhar(ctx):
  desenho = "desenhando"
  await ctx.send(desenho)
  Brasil = "🇧🇷"
  await ctx.send(Brasil)


@bot.command(name="caminhar")
async def caminhar(ctx):
   caminhar = "https://youtube.com/shorts/dNAb-854LD4?si=OyNulIfns687XdQa"
   await ctx.send(caminhar)
  

            
   




bot.run("TOKEN"):
#PARA CONSEGUIR O TOKEN ACESSE DISCORD/DEVLOPER COLOQUE A SUA CONTA DO DISCORD E CRIE UMA APLICAÇÃO E VA NA PAGINA BOT E CRIE O BOT E VA EM AUTH E CLIQUE EM BOT APLICIONCOMMANDS E COPIE O LINK PARA CONVINDAR O BOT E COLOQUE O SERVIDOR!
#USE !menu para saber o commandos



