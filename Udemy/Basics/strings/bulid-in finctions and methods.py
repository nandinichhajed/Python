quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.lower())
print(quote.find('be'))
print(quote.replace('be', 'me'))
print(quote)  # strings are immutable

quote2 = quote.replace('be', 'me')
print(quote2)
print(quote)

# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)
