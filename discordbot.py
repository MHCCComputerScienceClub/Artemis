import discord
import time
import datetime
import random
import config

name = "artemis"

print(name + ' is starting up...')

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ')')
    print('Connected to ' + str(len(client.servers)) + ' servers')
    print('Connected to ' + str(len(set(client.get_all_members()))) + ' users')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await client.send_message(message.channel, "Pong!")

    elif message.content.startswith('!about'):
        await client.send_message(message.channel, "I am " + name + ", a bot")

    elif message.content.lower() == "hi " + name + "!":
        await client.send_message(message.channel, "Hello " + message.author.mention + "!")

    elif message.content.lower() == "how are you " + name + "?":
        await client.send_message(message.channel, "I don't have emotions. I'm a robot.")
        time.sleep(0.5)
        await client.send_message(message.channel, "How are you, " + message.author.mention + "?")
    
    # Dice rolling script
    elif message.content.startswith("!roll"):
        try:
            splitmsg = message.content.split(' ')
            dice = int(splitmsg[1][1:] if splitmsg[1][0] == 'd' else splitmsg[1])
            if dice < 1:
                await client.send_message(message.channel, "You can't roll less than a one sided die!")
            elif dice > 1000:
                await client.send_message(message.channel, "That's too many sides for one die.")
            else:
                roll = random.randint(1, dice)
                if roll == 1:
                    await client.send_message(message.channel, str(roll) + " - critical fail!")
                elif roll == dice:
                    await client.send_message(message.channel, str(roll) + " - CRIT!")
                else:
                    await client.send_message(message.channel, str(roll) + "!")
        except ValueError:
            await client.send_message(message.channel, "That's not a number!")
        except IndexError:
            await client.send_message(message.channel, "Invalid usage. Use format `&roll d<number>`")

    # 8 Ball script - Orion
    elif message.content.lower().startswith(name) and message.content[-1] == '?':
        roll = random.randint(0,19)
        response = ["It is certain!",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes, definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy... try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again later.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        await client.send_message(message.channel, response[roll])

client.run(config.token)
