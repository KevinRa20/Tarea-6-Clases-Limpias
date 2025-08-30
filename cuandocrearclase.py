# 
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"Has prestado el libro: {self.titulo}"
        return "Este libro ya está prestado."

    def devolver(self):
        self.disponible = True
        return f"Has devuelto el libro: {self.titulo}"

# 
libro1 = Libro("Clean Code", "Robert C. Martin")
print(libro1.prestar())
print(libro1.devolver())
