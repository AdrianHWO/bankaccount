class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1

    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")


user1 = User("ShanShan", "Shanshan@gmail.com")
print(user1.display_user())

user2 = User("TunTun", "Tuntun@gmail.com")
print(user2.display_user())

print(User.user_count)
print(user1.user_count)
