import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
        elif message.content.startswith('!bot'):
            await message.channel.send('Wasspoppin {0.author.mention}'.format(message))

client = MyClient()
client.run('NzczOTg3MzE5NzA3MzM2NzE0.X6RN3Q.ti2IKe6nAdWBytaEs3LhF9u8cr8')