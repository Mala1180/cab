import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("cab")


class MyClass:
    def my_method(self):
        return "Hello World"


logger.info("cab loaded")
