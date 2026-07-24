# Work seamlessly with a multilingual repository 
from utils import somme_liste  # importing sum function from french module
from tests import função_teste # importing test function from portuguese module

if __name__ == "__main__":
    print("Sum of 1+2+3=", somme_liste([1, 2, 3]))
    print(função_teste("Hello there"))




