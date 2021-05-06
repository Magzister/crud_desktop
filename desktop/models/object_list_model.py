from copy import copy


class ObjectList:
    def __init__(self):
        self.object_list = None

    def get_list(self) -> list:
        if self.object_list:
            return copy(self.object_list)

    def get_list_item(self, ind: int):
        if self.object_list:
            try:
                element = copy(self.object_list[ind])
            except IndexError:
                return None
            return element

    def set_object_list(self, object_list: list):
        self.object_list = copy(object_list)
