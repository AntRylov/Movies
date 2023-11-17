import logging


#logging.basicConfig(
 #   level=logging.DEBUG,
  #  filename='my_log.log',
   # filemode='w',
    #format='%(asctime)s - %(levelname)s - %(message)s'
#)

logger = logging.Logger("new_logger")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = logging.FileHandler('my_log.log')
handler.setFormatter(formatter)


logger.addHandler(handler)


logger.info("Start application")
x = 20
y = 10

try:
    res = x / y
    logging.info("Succesfull operation .Result : {res}")
except ZeroDivisionError as err:
    logger.error(f"Error: {err} ")
else:
    print(res)

logging.debug("debug info")