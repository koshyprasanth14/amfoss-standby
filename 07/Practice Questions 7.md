Practice Questions 7

1.
the function "re.compile()" is called to create regex objects.

2.
raw strings are used as escape charaters will be used in the strings and we do not want the code to not considerthem.

3.
the search() method returns if a given string is present in an input string.

4.
using the group() function, we can get the actual strings that match the pattern from a Match object

5.
group 0 is the entire raw string : (\d\d\d)-(\d\d\d-\d\d\d\d)
group 1 is the first group enclosed in () : (\d\d\d)
group 2 is the second group enclosed in () :(\d\d\d-\d\d\d\d)

6.
by using a backslash in front of the required escape cahracter. for parantheses, it is \( and \), and for a period it is \.

7.
when the input string has no groups, the findall() function returns a list with the matched strings, and when there are groups, it returns a tuple with individual groups.

8.
it is a pipe character, and is used to match more than one strings.

9.
the ? character tells that the group precding it is optional. it can also be used in a lazy match.

10.
the + symbol matches all strings with 1 or more characters, while  matches 0 or more characters.

11.
{3} matches exactly 3 characters, and {3,5} matches 3,4, or 5 characters.

12.
\d signify digits, \w signify words, and \s signify whitespace.

13.
\D signify anything that is not digits, \W signify anything that is not words, and \S signify anything that is not whitespace.

14.
"." induces a greedy match where it identifies the longest match with the given condition, while ".?" induces a lazy match where it identifies the smallest match with the given condition.

15.
[0-9a-z]

16.
To make our regex case-insensitive, we can pass re.IGNORECASE or re.I as a second argument to re.compile().

17.
the . will match all characters except newline characters, and when DOTALL is passed as the second argument, it matches newlines too.

18.
X drummers, X pipers, five rings, X hens

19.
the variable re.VERBOSE tells the re.compile() function to ignore whitespace and comments inside the regular expression string.

20.
re.compiler(r'^\d{1,3}(\d{3})$')

21.
re.compiler(r'^[A-Z][a-z]\sWatanabe$')

22.
re.compile(r'^(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$', re.IGNORECASE)

23.
[Date Detection](./date.py)

24.
[Strong Password Detection](./password.py)

25.