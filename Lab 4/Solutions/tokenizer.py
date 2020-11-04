from enum import Enum

OPERATORS = ["+", "-", "*", "/"]

Token = Enum("Token", "EOF, START, DIGIT, DOT, NEGATION, OPERATOR, OPEN_BRACKET, CLOSE_BRACKET, NUMBER")

def basicTokenize(character):
    if character.isnumeric():
        return Token.DIGIT
    elif character == ".":
        return Token.DOT
    elif character == "(":
        return Token.OPEN_BRACKET
    elif character == ")":
        return Token.CLOSE_BRACKET
    # elif character == "-":
    #     return Token.NEGATION
    elif character in OPERATORS:
        return Token.OPERATOR
    elif character is Token.START:
        return character
    else:
        raise Exception(f"unexpected character {character}")

def tokenize(character, previousToken):
    try:
        currentToken = basicTokenize(character)
    except Exception as e:
        raise e

    if previousToken is Token.START:
        if currentToken in [Token.DIGIT, Token.OPEN_BRACKET, Token.NEGATION]:
            return currentToken
    if previousToken is Token.DIGIT:
        if currentToken in [Token.DIGIT, Token.DOT, Token.OPERATOR, Token.CLOSE_BRACKET]:
            return currentToken
    if previousToken is Token.DOT:
        if currentToken in [Token.DIGIT]:
            return currentToken
    if previousToken is Token.OPEN_BRACKET:
        if currentToken in [Token.DIGIT, Token.OPEN_BRACKET, Token.NEGATION]:
            return currentToken
    if previousToken is Token.CLOSE_BRACKET:
        if currentToken in [Token.OPERATOR, Token.CLOSE_BRACKET]:
            return currentToken
    if previousToken is Token.OPERATOR:
        if currentToken in [Token.DIGIT, Token.OPEN_BRACKET]:
            return currentToken
    # if previousToken is Token.NEGATION:
    #     if currentToken in [Token.DIGIT, Token.OPEN_BRACKET]:
    #         return currentToken

    raise Exception(f"unexpected character {character}")

def parse(characters):
    currentNumber = ""
    previousTokenType = Token.START
    tokens = []

    for currentCharacter in characters:
        try:
            token = tokenize(currentCharacter, previousTokenType)
            if token in [Token.DIGIT, Token.DOT]:
                currentNumber += currentCharacter
            elif currentNumber:
                tokens.append((Token.NUMBER,currentNumber))
                tokens.append((token,currentCharacter))
                currentNumber = ""
            else:
                tokens.append((token,currentCharacter))
            previousTokenType = token
        except Exception as e:
            print(e)
            break

    if currentNumber:
        tokens.append((Token.NUMBER,currentNumber))

    return tokens

def sanitize_expression(expression):
    return "".join(expression.split()).replace("()", "")
