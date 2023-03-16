# import utility
# import shopping.more_shopping.shopping_cart
# print(shopping.more_shopping.shopping_cart.buy('apple'))

# # another way
# import utility
# from shopping.more_shopping.shopping_cart import buy
# # package name # package name # module
# print(buy('apple'))

# # another way
# from utility import devide, multiply
# from shopping.more_shopping.shopping_cart import buy
# # package name # package name # module
# print(buy('apple'))
# print(devide(5, 2))
# print(multiply(5, 2))


# # another way (importing whole module)
# from utility import devide, multiply
# from shopping.more_shopping import shopping_cart
# # package name # package name # module
# print(shopping_cart.buy('apple'))
# print(devide(5, 2))
# print(multiply(5, 2))
