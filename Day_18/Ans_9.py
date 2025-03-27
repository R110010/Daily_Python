# Create a log file and write different levels of logs (INFO, ERROR).
import logging
logging.basicConfig(filename="app.log",filemode="a",level=logging.DEBUG)
logging.info(" this is a info log")
logging.warning(" this is a warning log")
logging.error(" this is a Error log")
logging.critical(" this is a critical log")
print(" logs have been written to the file")