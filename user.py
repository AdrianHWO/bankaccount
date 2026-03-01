class User:
    def __init__(self, username, email, password):
        self._username = username
        self._email = email  # Initialize using the internal name
        self.password = password

    @property
    def email(self):
        print("Email accessed")
        return self._email

    @email.setter
    def email(self, new_email):
        # 1. Check for "@" AND "." for better validation
        # 2. Assign to _email (with the underscore!) to avoid infinite loops
        if "@" in new_email and "." in new_email:
            self._email = new_email
        else:
            print(f"Invalid email: {new_email}. Update rejected.")


user1 = User("shanshan", "ShanShan@gmail.com", "1234")

# This will fail the check and print the warning
user1.email = "This is not email"

# This will work
user1.email = "new_shan@gmail.com"

print(f"Current email in system: {user1.email}")
