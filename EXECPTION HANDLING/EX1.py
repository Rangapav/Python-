# EXEPCTION HANDLING IS SIAD TO BE THE ERROR OCCURRED IN THE PROGRAM TO AVOID IT WE CAN USE TRY AND EXEPCT KEYWORDS

# THERE ARE DIFFERENT TYPES OF ERRORS
# 1>INDEX ERROR
# 2>SYNTAX ERROR-IF SYNTAX ERROR OCCURRED THE PROGRAM DOES NOT EXECUTE
# 3>IO ERROR
# 4>RUN TIME ERROR
# 5>INDENTATION ERROR
# 6>ZERO DIVISION ERROR

l=[1,2,3,4,5,6,7,8,9]

try:
    print(l[9])
except  IndexError:
    print("index error")
except  IOError:
    print("io error")
except ZeroDivisionError:
    print("Zero division error")
except KeyError:
    print("keyboard error")

except:
    print("error occurred")
finally:
    print("the code can execute every time ")
