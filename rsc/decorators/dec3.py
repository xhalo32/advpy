class Foo:
    def __init__(self):
        self.x = 42

foo = Foo()

def addto(instance):

    def decorator(f):
        import types

        f = types.MethodType(f, instance, instance.__class__)
        setattr(instance, f.func_name, f)

        return f

    return decorator

@addto(foo)
def print_x(self):
    print self.x

foo.print_x(  )