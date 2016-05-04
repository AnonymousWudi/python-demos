This is readme file. Contains all the the function of the examples in this folder.

==>example_1:

    In this example, you can get a result.txt file contains a picture that is drew by some codes. What you need to do is
just input an image you want to get.
    Command: python example_1.py filename.jpg(or some other types such as .png)


==>example_2:

    In this example, you can send email automatic or input information by yourself. This example can also send a email
contains attachment. You can change the code about the attachment name or something else.
    Command: python example_2.py (You need to input information by yourself. Not for parameters, but input.)


==>example_3:

    In this example, you can get something useful from the Internet! What I want to get is some books' information from
a website called DouBan. By compiling this program you can get top 250 books from website. But in the output text, I only
store the books which score is more than 8.5. I store the books' name, author, publishing houses, year and price.
    Command: python example_3.py


==>example_4:

    Write a function that returns all of the sublists of a list or Array.
    Your function should be pure; it cannot modify its input.
    Example:
        power([1,2,3])
        # => [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    For more details regarding this, see the power set entry in wikipedia.


==>example_5:

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


==>example_6:

    In the following 6 digit number:
        283910
    91 is the greatest sequence of 2 digits.

    Complete the solution so that it returns the largest five digit number found within the number given..
The number will be passed in as a string of only digits. It should return a five digit integer.
The number passed may be as large as 1000 digits.


==>example_7:

    Your task in order to complete this Kata is to write a function which formats a duration, given as a number of
seconds, in a human-friendly way.
    The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration
is expressed as a combination of years, days, hours, minutes and seconds.

    It is much easier to understand with an example:
        format_duration(62)    # returns "1 minute and 2 seconds"
        format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
    Note that spaces are important.

    Detailed rules

    The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and
one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.
    The components are separated by a comma and a space (", "). Except the last component, which is separated by
" and ", just like it would be written in English.
    A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is
not correct, but 1 year and 1 second is.
    Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.
    A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid,
but it should be just 1 minute.
    A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1
minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more
significant unit of time.
    For the purpose of this Kata, a year is 365 days and a day is 24 hours.


==>example_8:
    In this kata, you should calculate type of triangle with three given sides a, b and c (given in any order).
    If all angles are less than 90°, this triangle is acute and function should return 1.
    If one angle is strictly 90°, this triangle is right and function should return 2.
    If one angle more than 90°, this triangle is obtuse and function should return 3.
    If three sides cannot form triangle, or one angle is 180° (which turns triangle into segment) - function should return 0.

    Input parameters are sides of given triangle. All input values are non-negative floating point or integer numbers (or both).
    Examples:
    triangle_type(2, 4, 6) # return 0 (Not triangle)
    triangle_type(8, 5, 7) # return 1 (Acute, angles are approx. 82°, 38° and 60°)
    triangle_type(3, 4, 5) # return 2 (Right, angles are approx. 37°, 53° and exactly 90°)
    triangle_type(7, 12, 8) # return 3 (Obtuse, angles are approx. 34°, 106° and 40°)
    If you stuck, this can help you: http://en.wikipedia.org/wiki/Law_of_cosines. But you can solve this kata even without angle calculation.
    There is very small chance of random test to fail due to round-off error, in such case resubmit your solution.


==>example_9:
    Create a RomanNumerals helper that can convert a roman numeral to and from an integer value. The class should
follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.
    Modern Roman numerals are written by expressing each digit separately starting with the left most digit and
skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

    Examples:
    RomanNumerals.to_roman(1000) # should return 'M'
    RomanNumerals.from_roman('M') # should return 1000
