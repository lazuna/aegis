import re

def password_strength(password):
    if len(password) < 8:
        return "Password too short!"
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter!"
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter!"
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one digit!"
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special character!"
    return "Password is strong."

password = 'P@ssw0rd123'
strength = password_strength(password)
print(f"Password strength: {strength}")
