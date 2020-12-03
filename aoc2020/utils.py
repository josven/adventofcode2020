from functools import wraps
from timeit import default_timer


def time_this(func):

	@wraps(func)
	def wrap(*args, **kwargs):
		start_time = default_timer()
		result = func(*args, **kwargs)
		time = round((default_timer() - start_time) * 1000, 3)
		print(f"{func.__name__} took {time} ms")
		return result

	return wrap
