SPECIAL_CHARS = "[]{}"
WHITESPACE = " \t\n\r\v"

def singleChar(check):
    def wrapper(char:chr):
        if len(char) != 1:
            raise(NameError("Must be a single character"))
        return(check(char))
    return(wrapper)

@singleChar
def isSpec(char):
    return(char in SPECIAL_CHARS)

@singleChar
def isWs(char):
    return(char in WHITESPACE)

@singleChar
def isLetter(char):
    return(not (isSpec(char) or isWs(char)))

def isWord(string):
    return(all(isLetter(i) for i in string))

def isWsBlock(string):
    return(all(isWs(i) for i in string))

def tokenise(text):

    def charType(char):
        if isWs(char):
            return(isWsBlock,"WHITESPACE")
        elif isLetter(char):
            return(isWord,"WORD")
        else:
            return("SYMBOL")

    textPos = 0
    text += " "
    targetLength = len(text)
    chunks = []

    def scan(args):

        rule = args[0]
        name = args[1]
        nonlocal textPos
        currentStr = text[textPos]

        while textPos < targetLength and rule(currentStr):

            textPos += 1
            try:
                currentStr += text[textPos]
            except IndexError:
                return("","EOF")

        currentStr = currentStr[:-1]
        return(currentStr,name)

    while textPos < targetLength:

        currentChr = text[textPos]
        curCharType = charType(currentChr)
        if curCharType == "SYMBOL":
            chunks.append((currentChr,"SYMBOL"))
            textPos += 1
        else:
            chunks.append(scan(curCharType))

    return(chunks)
