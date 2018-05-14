def smallStuff(message, NAME):
    if message.content.startswith('!ping'):
        return "Pong!"

    elif message.content.startswith('!about'):
        return "I am " + NAME + ", a bot"

    elif message.content.lower() == "hi " + NAME + "!":
        return "Hello " + message.author.mention + "!"

    elif message.content.lower() == "how are you " + NAME + "?":
        return "I don't have emotions. I'm a robot."
        time.sleep(0.5)
        return "How are you, " + message.author.mention + "?"

    elif message.content.lower().startswith("good bot"):
        return "Thank you, " + message.author.mention

    elif message.content.lower().startswith("bad bot"):
        return "I'm sorry, I'll try to do better next time :frowning:"
    else:
        return False
