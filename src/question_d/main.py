#add import
def use_global():
    globals()["global_x"] = 500
    
global_x = 15
print("The global variable x originally was ", globals()["global_x"])
use_global()
print("The global variable x is now ", globals()["global_x"])