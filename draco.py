import requests
import discord #importamos para conectarnos con el bot
from discord.ext import commands #importamos los comandos
import datetime 
import asyncio


bot = commands.Bot(command_prefix='_', description="Wemix Draco Price Track")

class Crypto_Price:
    def get_price(url, crypto):
        request = requests.post(url, verify=False)
        response_json = request.json()
        crypto_price  = response_json['Data'][crypto]
        print(request)
        # print(peticion.text)Ws
        print(type(crypto_price))
        request.close()
        return crypto_price[0:4]

# Get Price
draco_wemix_price = Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/draco/lastest' , 'USDDracoRate')
"${0:3} USD".format(draco_wemix_price)

hidra_wemix_price = Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/hydra/lastest' , 'USDHydraRate')
"${0:3} USD".format(hidra_wemix_price)

# Discord
# Bot commands
@bot.command()
async def wemix(ctx):
     await ctx.send("${} USD Wemix".format(Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/draco/lastest' , 'USDWemixRate')))

@bot.command()
async def klay(ctx):
     await ctx.send("${} USD Klay".format(Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/draco/lastest' , 'USDKLAYRate')))

@bot.command()
async def price(ctx):
     await ctx.send("${} USD Draco Wemix".format(Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/draco/lastest' , 'DracoPriceWemix')))
     await ctx.send("${} USD Draco Oficial Web".format(Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/draco/lastest' , 'USDDracoRate')))
     await ctx.send("${} USD Klay".format(Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/draco/lastest' , 'USDKLAYRate')))
     await ctx.send("${} USD Wemix Credit".format(Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/draco/lastest' , 'USDWemixRate')))
     await ctx.send("${} USD Hidra".format(Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/hydra/lastest' , 'USDHydraRate')))

@bot.command()
async def draco(ctx):
     await ctx.send("${} USD Draco".format(Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/draco/lastest' , 'USDDracoRate')))

@bot.command()
async def hidra(ctx):
     await ctx.send("${} USD Hidra".format(Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/hydra/lastest' , 'USDHydraRate')))

@bot.command()
async def calculate(ctx,  amount = 0, coin = "draco"):
     coin = coin.lower()
     if coin == "draco":
          await ctx.send("${0:3} USD".format(float((Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/draco/lastest' , 'USDDracoRate')))*amount))
     if amount == 150:
          await ctx.send("Esal e viado")
     if coin == "klay":
          await ctx.send("${0:3} USD".format(float((Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/draco/lastest' , 'USDKLAYRate')))*amount))



# Show price in discord
@bot.event
async def on_ready():
    while True:
          try:
               draco_price = None
               draco_wemix_price = None
               klay_price = None
               await asyncio.sleep(5)
               draco_price = Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/draco/lastest' , 'USDDracoRate')
               await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "${} USD|Draco".format(draco_price)))
               await asyncio.sleep(5)
               draco_wemix_price = Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/draco/lastest' , 'DracoPriceWemix')
               await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "${} USD|Wemix Draco".format(draco_wemix_price)))
               await asyncio.sleep(5)
               klay_price = Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/draco/lastest' , 'USDKLAYRate')
               await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "${} USD|Klay".format(klay_price)))
               await asyncio.sleep(5)
               wemix_price = Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/draco/lastest' , 'USDWemixRate')
               await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "${} USD|Wemix Credit".format(wemix_price)))
               await asyncio.sleep(5)
               hidra_price = Crypto_Price.get_price('https://api.mir4global.com/wallet/prices/hydra/lastest' , 'USDHydraRate')
               await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "${} USD|Hidra".format(hidra_price)))
          except:
               pass
          

          # Security
bot.run('secret')
