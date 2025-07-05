from functools import lru_cache
import time
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*5
 #lru cache used when we don't want to compute the value more then one time either we run it more then one time
 #lru cache compute the value only one time in anywhere in program, it store the value in memory , if we print or compute the same value in anywhere in program it doesn't take time and it doesn't compute it take the value from past value from the memory
print(fx(3))
print("Done for 3")
print(fx(4))
print("Done for 4")
print(fx(5))
print("Done for 5")
#like here at above we compute the value 
print(fx(3))
print("Done for 3")
print(fx(4))
print("Done for 4")
print(fx(5))
print("Done for 5")
#and here we also compute the value but it doesn't take time because it take the value from past value from the memory 