from db import * 

init_db()

set_user(1238456, "test_user", "Test", "User", "male", 30, 70.5, 175.0, "moderate", "maintain", 1500.0, 1800.0, 1700.0)

set_user(4896589, "test_user", "Test", "User", "male", 30, 70.5, 175.0, "moderate", "maintain", 1500.0, 1800.0, 1700.0)

set_user(4854789, "test_user", "Test", "User", "male", 30, 70.5, 175.0, "moderate", "maintain", 1500.0, 1800.0, 1700.0)

print(get_user(1238456))
