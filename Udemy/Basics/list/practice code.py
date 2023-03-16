basket = ['Banana', "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
basket.pop()
basket.extend(['Kiwi'])
basket.insert(0, 'Apples')
print(basket.count('Apples'))
print(basket)
basket.clear()
print(basket)
