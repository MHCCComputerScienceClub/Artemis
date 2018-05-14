CODEWEIGHT = 0.21
PLAINWEIGHT = 0.03191 
PLCDRATIO = (PLAINWEIGHT + CODEWEIGHT) / 2 # Plain to code ratio
SPECIALSET = "[]{};:\"/<>|\\-_=+#$%^&*()@~`"

def formatCode(message):
    # Create a count for each character 
    charCount = {}
    for char in message.content:
        if(char in charCount):
            charCount[char] += 1
        else:
            charCount[char] = 1
    specialCount = 0

    # Add up the number of special character occurances
    for char in SPECIALSET:
        if(char in charCount):
            specialCount += charCount[char]

    # Generate a ratio of special to nonspecial
    ratio = specialCount/(len(message.content)*1.0)

    if ratio > PLCDRATIO:
        return ("Excuse me, good sir. I " +
        "believe you forgot to format your code. I'll do it for you " +
        "this time, but next time remember to begin and end your code with " +
        "'\`\`\`' for multiple lines of code, or a single '\`' for inline " +
        "code.\n ```" + message.content +
        '```\n\nRatio of special to non-special: ' +
        str(round(ratio*100, 2)) + "%" +  # Ratio of special characters to nonspecial ones
        ' | Confidence: ' + 
        str(round((ratio/(CODEWEIGHT - PLAINWEIGHT)) * 100, 2)) + '%') # Confidence level
