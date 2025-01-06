import budgeter
import cfuncs
from error import *

def main():
    # get c funcs figured out
    try:
        budgeter.main()
    except Error as e: # diff types of error
        cfuncs.error_save(e.dump)
    return 0

if __name__ == "__main__":
    main()