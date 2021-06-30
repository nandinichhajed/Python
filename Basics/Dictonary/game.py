# 1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys:
# 'age', 'username', 'weapons', 'is_active' and 'clan'

profile = {
    'age': 20,
    'user_name': 'Nandini',
    'weapons': ['gun', 'bomb'],
    'is_active': True,
    'clan': 'India'
}
# 2 iterate and print all the keys in the above user.
print(profile.keys())
# 3 Add a new weapon to your user
profile['weapons'].append('arrow')
print(profile)
# 4 Add a new key to include 'is_banned'. Set it to false
profile.update({'is_banned': False})
print(profile.keys())
# 5 Ban the user by setting the previous key to True
profile['is_banned'] = True
print(profile)
# 6 create a new user2 my copying the previous user and update the age value and username value.
profile2 = profile.copy()
profile2.update({'age': 22, 'user_name': 'Nanni'})
print(profile2)
