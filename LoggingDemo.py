import  logging
logging.basicConfig(
    filename="myfile.log",
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def factorial(n):
    if n<0:
        logging.error("Input value never be less than 0")
        return None

    elif n == 0:
        if n == 0:
            logging.warning("Factorial of 0 is 1")
            return 1

    else:
        result = 1
        for i in range(1,n+1):
            result *=i
        return result



n = 5
fac=factorial(n)
fac = result +i


