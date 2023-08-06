import requests
import timeit


def timer(fn):
    def wrapper(*args, **y):
        start_time = timeit.default_timer()
        cached_value = fn(*args, **y)
        end_time = timeit.default_timer()
        print("It took {} seconds to run".format(end_time - start_time))
        return cached_value
    return wrapper


@timer
def do_something(url):
    response = requests.get(url)
    return len(response.text)


# do_something = timer(do_something)

url = "https://www.google.co.uk"
print(do_something(url))
url = "https://www.eldiario.es/"
print(do_something(url))
