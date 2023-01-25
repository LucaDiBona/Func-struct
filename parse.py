def preparse(tokens):
    return([x for x in tokens if x[1]!="WHITESPACE"])

def parse(tokens):

    wordPos = 0
    output = ""

    def openB(_):
        return("\\begin{bmatrix}")

    def closeB(_):
        return("\\end{bmatrix}\\\\")

    def openC(_):
        return("\\begin{Bmatrix}")

    def closeC(_):
        return("\\end{Bmatrix}\\\\")

    def word(word:str):
        nonlocal wordPos

        if wordPos == 0:
            wordPos = 1
            return(f"\\text{{word.upper()}} & ")

        else:
            wordPos = 0
            return(f"\\text{{word}}\\\\")

    COMMANDS = {"[":openB,"]":closeB,"{":openC,"}":closeC}

    for i in tokens:

        if i[1] == "SYMBOL":
            output += COMMANDS[i[0]](0)

        else:
            output += word(i[0])

    return(output[:-2])





