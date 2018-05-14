def rollDice(message):
    try:
        splitmsg = message.content.split(' ')
        dice = int(splitmsg[1][1:] if splitmsg[1][0] == 'd' else splitmsg[1])
        if dice < 1:
            return "You can't roll less than a one sided die!"
        elif dice > 1000:
            return "That's too many sides for one die."
        else:
            roll = random.randint(1, dice)
            if roll == 1:
                return str(roll) + " - critical fail!"
            elif roll == dice:
                return str(roll) + " - CRIT!"
            else:
                return str(roll) + "!"
    except ValueError:
        return "That's not a number!"
    except IndexError:
        return "Invalid usage. Use format `&roll d<number>`"
