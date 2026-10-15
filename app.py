def add(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}! Welcome to the DevOps pipeline."

def login(email, password):
    return bool(email) and len(password) >= 6

if __name__ == "__main__":
    print(greet("Student"))