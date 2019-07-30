import time

global_timeit_depth = -1

def timeit(method):
    def timed(*args, **kw):
        global global_timeit_depth
        global_timeit_depth += 1
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('----'*global_timeit_depth + '|'
                  + f'{method.__name__} '
                  + f'{(te - ts) * 1000:.2f} ms')
            global_timeit_depth -= 1
        return result
    return timed
