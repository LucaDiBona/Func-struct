import sys, tokenise, parse

x = input(">> ")
print(parse.parse(parse.preparse(tokenise.tokenise(x))))