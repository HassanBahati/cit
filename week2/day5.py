'''
Unicode is an industry standard for consistent encoding of written text
is the first of its kind to aim to support every single written language
'''

#Converting a string into UTF-8 and printing it
city = 'kampala'
print(city.encode('utf-8'))

'''
outputting emoji with no imports
printing out emojis with CLDR names
'''
print('hello', '\N{winking face}')
print('\U0001F923')

