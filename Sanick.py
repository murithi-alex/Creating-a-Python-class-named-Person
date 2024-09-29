from sanic import Sanic
from sanic.response import text

app = Sanic("PersonApp")

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}."

@app.route("/")
async def handle_request(request):
    person = Person("Alice Doe", 22, "Female")
    return text(person.introduce())

if __name__ == "__main__":
    app.run(host="localhost", port=8000)
