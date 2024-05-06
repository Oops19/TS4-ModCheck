#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


class ModCheckSingleton(type):
    """Any instances created using this class will be of a single instance.


    :Example usage:

    .. highlight:: python
    .. code-block:: python

        class Foo(metaclass=BBSingleton):
            def __init__(self):
                self.state = 0

        f = Foo()
        f.state = 3
        g = Foo()
        g.state == 3  # True

    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(ModCheckSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
