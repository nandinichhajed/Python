# Design a rating system, where user is asked to
# rate a product between 1 and 5. Following are the
# feedback that we want to give users.
# 1. Sorry to hear about your experience
# 2. We are trying to get better
# 3. Thanks
# 4. We almost missed the perfect rating from you
# 5. Happy to know that you loved our services


user_rating = int(input("Enter the rating B/W 1-5: "))

if user_rating == 1:
    print("Sorry to hear about your experience")

elif user_rating == 2:
    print("We are trying to get better")

elif user_rating == 3:
    print("Thanks")

elif user_rating == 4:
    print("We almost missed the perfect rating from you")

elif user_rating == 5:
    print("Happy to know that you loved our services")
else:
    print("Please enter rating b/w 1-5 only")