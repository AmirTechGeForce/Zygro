import discord, os
from life import revive_stamina
from prsaw import RandomStuff

rs = RandomStuff()
client = discord.Client(async_mode = True)
res = rs.get_ai_response("Hi there!")

@client.event
async def on_ready():
  print("Let's go, {0.user}!".format(client))

@client.event
async def on_message(message):
  if client.user == message.author:
    return
    
  res = rs.get_ai_response(message.content)
  await message.reply(res)

revive_stamina()
client.run(os.getenv('TOKEN'))
