# coding=utf-8


class RomanNumerals():

    @staticmethod
    def to_roman(number):
        s = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
         ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
         ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
         ["", "M", "MM", "MMM"]]
        string = ''
        string += s[3][number / 1000 % 10]
        string += s[2][number / 100 % 10]
        string += s[1][number / 10 % 10]
        string += s[0][number % 10]
        return string

    @staticmethod
    def from_roman(string):
        result = 0
        for i in range(len(string)):
            if string[i] == 'M':
                result += 1000
            elif string[i] == 'D':
                result += 500
            elif string[i] == 'C':
                if i == len(string) - 1:
                    result += 100
                elif string[i+1] == 'D' or string[i+1] == 'M':
                    result -= 100
                else:
                    result += 100
            elif string[i] == 'L':
                result += 50
            elif string[i] == 'X':
                if i == len(string) - 1:
                    result += 10
                elif string[i+1] == 'L' or string[i+1] == 'C':
                    result -= 10
                else:
                    result += 10
            elif string[i] == 'V':
                result += 5
            elif string[i] == 'I':
                if i == len(string) - 1:
                    result += 1
                elif string[i+1] == 'V' or string[i+1] == 'X':
                    result -= 1
                else:
                    result += 1
        return result


if __name__ == '__main__':
    print RomanNumerals.to_roman(2008)
    print RomanNumerals.from_roman("MDCLXVI")
