
def get_inputs():
    random_state = 42
    n_splits = 2
    n_iter = 50
    test_size = 0.2
    lgbm_prefix = "LGBM"
    return locals()


class InputHanger(object):
    class _InnerInputHanger(object):

        def __init__(self):
            for parameter, value in get_inputs().items():
                setattr(self, parameter, value)
    instance = None

    def __new__(cls):  # __new__ is always a class method
        if not InputHanger.instance:
            InputHanger.instance = cls._InnerInputHanger()
        return InputHanger.instance
