class Cookie:
    def __init__(self, color) -> None:
        self.color = color

    def get_color(self) -> str:
        return self.color
    
    def set_color(self, color):
        self.color = color

    def __str__(self) -> str:
        return f"It is a cookie of {self.color} color."

cookie_one = Cookie("green")
cookie_two = Cookie("blue")

print("Cookie one is", cookie_one.get_color())
print("Cookie two is", cookie_two.get_color())

cookie_one.set_color("yellow")

print("Cookie one is now", cookie_one.get_color())
print("Cookie two is still", cookie_two.get_color())

print(cookie_one)
print(cookie_two)