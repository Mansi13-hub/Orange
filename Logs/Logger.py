
import inspect
import logging

class LogGen:
    @staticmethod
    def loggen():
        classname=inspect.stack()[1][3]
        logger=logging.getLogger(classname)
        file=logging.FileHandler("C:\\Users\\Suraj V. Chaudhari\\Desktop\\Orange\\Logs\\l.log")
        #format=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(function)s : %(message)s")
        logging.basicConfig(filename="C:\\Users\\Suraj V. Chaudhari\\Desktop\\Orange\\Logs\\l.log",format="%(asctime)s : %(levelname)s : %(name)s : %(function)s : %(message)s",filemode='w'
    )

       # file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger