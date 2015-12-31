'''def simple_decorator(decorator):

	def new_decorator(f):
		g = decorator(f)
		g.__name__ = f.__name__
		g.__doc__ = f.__doc__
		g.__dict__.update(f.__dict__)
		return g

	new_decorator.__name__ = decorator.__name__
	new_decorator.__doc__ = decorator.__doc__
	new_decorator.__dict__.update(decorator.__dict__)
	return new_decorator'''

def why_the_heck_was_the_simple_decorator_in_here( decorator ):

	print decorator.__name__
	return decorator

@why_the_heck_was_the_simple_decorator_in_here
def my_simple_logging_decorator(func):

	def asdf(*args, **kwargs):

		print 'calling {}'.format(func.__name__)
		return func(*args, **kwargs)

	return asdf

@my_simple_logging_decorator
def asdf(x):

	for i in range( x ):
		print "asdf"

asdf(1)