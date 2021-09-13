from sys import stdout
class console:
    def log(*arguments, **jsimpli):
        term = jsimpli.pop("file", None)
        if term is None:
            term = stdout
            if term is None:
                return
        def inject(info):
            term.write(str(info))
        sep = jsimpli.pop("sep", None)
        if sep is not None:
            if not isinstance(sep, str):
                raise TypeError("always None or a string")
        end = jsimpli.pop("end", None)
        if end is not None:
            if not isinstance(end, str):
                raise TypeError("always None or a string")
        flush = jsimpli.pop('flush', None)
        if jsimpli:
            raise TypeError("invalid keyword arguments to log()")
        if sep is None:
            sep = " "
        if end is None:
            end = "\n"
        for i, arg in enumerate(arguments):
            if i:
                inject(sep)
            inject(arg)
        inject(end)
        if flush:
            term.flush()

