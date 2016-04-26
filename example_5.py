# coding=utf-8


def validBraces(string):
    list = []
    for i in string:
        if i == '(' or i == '[' or i == '{':
            list.append(i)
        elif i == ')' and list and list[-1] == '(':
            list.pop()
        elif i == ']' and list and list[-1] == '[':
            list.pop()
        elif i == '}' and list and list[-1] == '{':
            list.pop()
        else:
            return False
    return True if not list else False

if __name__ == '__main__':
    print validBraces(")(}{][")
