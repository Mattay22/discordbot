import discord
import responses
from datetime import datetime

async def new_rumour(message, user_message, username, timestamp):
    user_message = user_message.replace('<@1193176493430423635> ', '')
    user_message = user_message.replace('#transferrumour', '')
    timestamp = timestamp.split(".")[0]
    user_message = f"@{username} : {user_message} [{timestamp}]"
    f = open("log.txt", "a")
    f.write(f'\n{user_message}')
    f.close()
    
    await message.channel.send('Rumour recieved')
    
async def summary(message, user_message, storage_channel, timestamp):
    
    await message.channel.send('Todays Transfer Rumours:')
    f = open("log.txt", "r")
    for i in f:
        i = str(i)
        today = datetime.today().strftime('%Y-%m-%d')
        today = str(today)
        if today in i:
            await message.channel.send(i)


async def historic_summary(message, user_message, storage_channel, timestamp):

    await message.channel.send('Transfer Rumours:')
    f = open("log.txt", "r")
    for i in f:
        i = str(i)
        await message.channel.send(i)       

async def help(message):

    await message.channel.send('Hey im Lenno Bot. To add a new transfer rumour, please tag me and use #transferrumour, for a summary of todays transfers please use #transfersummary, for previous days please use #historictransfersummary. For any other issues please contact @mattay22')


def run_discord_bot():
    
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!!!')

    @client.event
    async def on_message(message):

        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        timestamp = str(message.created_at)
        user_message = user_message.lower()
        if '<@1193176493430423635' not in user_message:
            return
        print(f"{username} said: '{user_message}' ({channel})")
        storage_channel = client.get_channel(1193210556988006400)
        if "#transferrumour" in user_message:
            await new_rumour(message, user_message, username, timestamp)
        if "#transfersummary" in user_message:
            await summary(message, user_message, username, timestamp)
        if "#historictransfersummary" in user_message:
            await historic_summary(message, user_message, username, timestamp)
        if "#help" in user_message:
            await help(message)
 



    client.run(TOKEN)