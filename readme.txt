This is readme file. Contains all the the function of the examples in this folder.

example_1:
    In this example, you can get a result.txt file contains a picture that is drew by some codes. What you need to do is
just input an image you want to get.
    Command: python example_1.py filename.jpg(or some other types such as .png)

example_2;
    In this example, you can send email automatic or input information by yourself. This example can also send a email
contains attachment. You can change the code about the attachment name or something else.
    Command: python example_2.py (You need to input information by yourself. Not for parameters, but input.)

example_3:
    In this example, you can get something useful from the Internet! What I want to get is some books' information from
a website called DouBan. By compiling this program you can get top 250 books from website. But in the output text, I only
store the books which score is more than 8.5. I store the books' name, author, publishing houses, year and price.
    Command: python example_3.py

example_4:
    Write a function that returns all of the sublists of a list or Array.
    Your function should be pure; it cannot modify its input.
    Example:
        power([1,2,3])
        # => [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    For more details regarding this, see the power set entry in wikipedia.

example_5:
    Write a function called validBraces that takes a string of braces, and determines if the order of the braces is
valid. validBraces should return true if the string is valid, and false if it's invalid.

    This Kata is similar to the Valid Parentheses Kata, but introduces four new characters. Open and closed brackets,
and open and closed curly braces. Thanks to @arnedag for the idea!

    All input strings will be nonempty, and will only consist of open parentheses '(' , closed parentheses ')', open
brackets '[', closed brackets ']', open curly braces '{' and closed curly braces '}'.

    What is considered Valid? A string of braces is considered valid if all braces are matched with the correct brace.
    For example:
        '(){}[]' and '([{}])' would be considered valid, while '(}', '[(])', and '[({})](]' would be considered invalid.

    Examples:
    validBraces( "(){}[]" ) => returns true
    validBraces( "(}" ) => returns false
    validBraces( "[(])" ) => returns false
    validBraces( "([{}])" ) => returns true