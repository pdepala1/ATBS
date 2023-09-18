import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(message)
print(mo)
print(mo.group())
print(phoneNumRegex.findall(message))
print(mo.group(1))
print(mo.group(2))

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel.')
print(mo.group())
print(mo.group(1))

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowoman')
print(mo == None)

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group())

mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo == None)

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
print(phoneRegex.search('My phone  number is 415-555-1234. Call me tomorrow.'))
print(phoneRegex.search('My phone number is 555-1234. Call me tomorrow.'))

batRegex = re.compile(r'Bat(wo)*man')
print(batRegex.search('The Adventure of Batman'))
print(batRegex.search('The Adventure of Batwoman'))
print(batRegex.search('The Adventure of Batwowowoman'))

batRegex = re.compile(r'Bat(wo)+man')
print(batRegex.search('The Adventures of Batman'))
print(batRegex.search('The Adventures of Batwoman'))
print(batRegex.search('The Adventures of Batwowowoman'))

regex = re.compile(r'\+\*\?')
print(regex.search('I learned about +*? regex syntax'))
regex = re.compile(r'(\+\*\?)+')
print(regex.search('I learned about +*?+*?+*?+*? regex syntax'))

haRegex = re.compile(r'(Ha){3}')
print(haRegex.search('He said "HaHaHa"'))

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')#Find 3 instances, maybe a comma too
print(phoneRegex.search('My numbers are 415-555-1234,555-4242,212-555-0000'))

haRegex = re.compile(r'(Ha){3,5}') #Min 3 occurances Max 5
print(haRegex.search('He said "HaHaHa"'))
print(haRegex.search('He said "HaHaHaHaHa"'))
print(haRegex.search('He said "HaHaHaHaHaHaHa"'))

haRegex = re.compile(r'(Ha){3,}') #Minimum 3 no max
print(haRegex.search('He said "HaHaHaHaHaHaHaHa"'))

digitRegex = re.compile(r'(\d){3,5}') #Greedy match
print(digitRegex.search('1234567890'))
digitRegex = re.compile(r'(\d){3,5}?') #? for non-Greedy match
print(digitRegex.search('1234567890'))

# Resume phone numbser parsing

resume = 'blah blah 508-555-5555 bhal blah blah 508-555-1234 wsojgfwqeff '

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex)
print(phoneRegex.findall(resume))
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall(resume))
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(resume))

lyrics = "12 lords a-leaping, 11 ladies dancing, 10 pipers piping 9 drummers drumming, 8 maids a-milking 7 swans a-swimming, 6 geese a-laying And 5 gold rings, 4 calling birds, 3 French hens, 2 turtle doves And 1 partridge in a pear tree, and a partridge in a pear tree"

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))


regexObj = re.compile(r'[aeiouAEIOU]')# same as r'(a|e|i|o|u)'
print(regexObj.findall('Robocop eats baby food'))
regexObj = re.compile(r'[aeiouAEIOU]{2}')
print(regexObj.findall('Robocop eats baby food'))
regexObj = re.compile(r'[^aeiouAEIOU]')
print(regexObj.findall('Robocop eats baby food'))

beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))
print(beginsWithHelloRegex.search('He said "Hello!"'))

endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search('Hello world!'))
print(endsWithWorldRegex.search('Hello world!swewfewfwegf'))

allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('25874328597234587'))
print(allDigitsRegex.search('258743285x97234587'))

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

nametext = 'First Name: Al Last Name: Sweigart'
print(nametext.find(':'))
print(nametext.find(':')+2)
print(nametext[12:])

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall(nametext))

serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))
greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

prime = 'Serve the public trust. \nProtect the innocent. \nUphold the law.'
print(prime)

dotStar = re.compile(r'.*')
print(dotStar.search(prime))
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))

vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.search('Al why does your programming book talk about Robocop so much?'))
print(vowelRegex.findall('Al why does your programming book talk about Robocop so much?'))
vowelRegex = re.compile(r'[aeiou]', re.I)
print(vowelRegex.findall('Al why does your programming book talk about Robocop so much?'))

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.'))

re.compile(r'''
   (\d\d\d-)|  # area code
   (\(\d\d\d\))  # -or- area code with parens and no dash
   \d\d\d       # first 3 digits
   -       # second dash
   \d\d\d\d # last 4 digits
   \sx\d{2,4} # extension, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE)