from classes import User, Privileges, Admin

# mr_k = Admin('Kyle', 'Huber', 29, 'brown', 0)
# mr_k.privileges.show_privileges()

user_1 = User('Kyle', 'Huber', 29, 'dark brown', 0)
user_2 = User('Stephen', 'Huber', 27, 'chestnut', 0)

user_1.describe_user()
user_2.greet_user()
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(2)
user_1.increment_login_attempts(10)
user_1.increment_login_attempts(0)
user_1.reset_login_attempts()