from sys import stdout
class console:
    def log(*args, **kwargs):
        term = kwargs.pop("file", None)
        if term is None:
            term = stdout
            if term is None:
                return
        def write(data):
            term.write(str(data))
        sep = kwargs.pop("sep", None)
        if sep is not None:
            if not isinstance(sep, str):
                raise TypeError("always None or a string")
        end = kwargs.pop("end", None)
        if end is not None:
            if not isinstance(end, str):
                raise TypeError("always None or a string")
        flush = kwargs.pop('flush', None)
        if kwargs:
            raise TypeError("invalid keyword arguments to log()")
        if sep is None:
            sep = " "
        if end is None:
            end = "\n"
        for i, arg in enumerate(args):
            if i:
                write(sep)
            write(arg)
        write(end)
        if flush:
            term.flush()

