import logging

class Micro_Logger():
    def __init__(self):
        # Step 1: Loggers, 并设置全局level
        self.logger = logging.getLogger('logging_blog')
        self.logger.setLevel(logging.DEBUG)
        # Step 2: Handler
        # print to screen
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # # write to file
        fh = logging.FileHandler("log_file.log")
        fh.setLevel(logging.DEBUG)

        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def change_level(self, level):
        self.logger.setLevel(level)

    def exception(self, message):
        self.logger.exception(message)



def a():
    raise Exception("888888")

def b():
    a()

if __name__ == "__main__":
    logger = Micro_Logger()
    logger.debug("this is debug")
    logger.info("this is info")
    logger.warning("this is warning")
    logger.error("this is error")
    logger.change_level(logging.ERROR)
    logger.debug("this is debug")
    logger.info("this is info")
    logger.warning("this is warning")
    logger.error("this is error")

    try:
        b()
    except:
        logger.exception("this is exception test")


