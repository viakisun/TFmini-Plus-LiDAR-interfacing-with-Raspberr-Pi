# class MetaSingleton(type):
#     _instance = {}
    
#     def __call__( cls, *args, **kwargs):
#         if cls not in cls._instance:
#             cls._instance[cls] = super( MetaSingleton, cls).__call__( *args, **kwargs)
#         return cls._instance[cls]

# class Box( metaclass = MetaSingleton):
#     __box = {}
    
#     def add(self, key, value):
#         self.__box[key] = value

#     def get(self, key):
#         return self.__box[key]
    
#     def remove(self, key):
#         self.__box.pop(key)
    
#     def show(self):
#         for d in self.__box:
#             print( d)

# b1 = Box()
# b2 = Box()
# b3 = Box()

# b1.add("1", "test1")
# b2.add("2", "test2")
# b3.add("3", "test3")

# b1.show()
# b2.show()
# b3.show()

from config_manager import *

c1 = ConfigManager()
print(c1.get_value('spray_mode'))


