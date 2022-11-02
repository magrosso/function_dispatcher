class Device:
    _instance_count = 0

    def __init__(self):
        Device._instance_count += 1
        print(f'{__name__}: Created Device instance {Device._instance_count}')

    def get_attribute(self, cmd: str, parm: int):
        get_method_name = 'get_' + cmd
        try:
            get_method = getattr(self, get_method_name)
            return get_method(parm)
        except AttributeError as att_err:
            print(f'Method {get_method_name}() not found: {att_err}')

    def get_attribute_1(self, num: int) -> int:
        return num

    def get_attribute_2(self, num: int) -> int:
        return num


dev = Device()
