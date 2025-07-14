import discord

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTM4MjA1MDE2OTEzODQ0NjM0Ng.GFAIgp.9FMGfrRkfuAXFfCNdYUdPE67HshXw7xnwcYL6E') # Replace with your own token.
