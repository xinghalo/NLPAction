class FooBar:
    def __init__(self):
        self.somvar = 42
f = FooBar()
print f.somvar

class FooBar2:
    def __init__(self, value=42):
        self.somevar = value
f1 = FooBar2()
print f1.somevar