# Varargs

def varargs(fir, sec, *args):
    print(fir, sec)
    print(args)


def create_dict(fir, sec, **kwargs):  # keyword arguments **kwargs:
    print(fir, sec)
    print(kwargs)
    m_dict = {}


# varargs(1, 2, 3, 4, 5)
# parameter name must be specified key = value (**kwargs)
s = ('s', 5)
t = ('t', 6)
create_dict(fir=1, sec=2, s=s, t=t)
