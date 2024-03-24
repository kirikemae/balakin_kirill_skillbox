import logging
import json
from datetime import datetime

class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        message = json.dumps({"time": datetime.now().strftime("%H:%M:%S"),
                              "level": kwargs.get("extra")["level"],
                              "message": msg}, ensure_ascii=False)

        return message, kwargs


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(message)s",
                        filename="skillbox_json_messages.log")
    logger = JsonAdapter(logging.getLogger(__name__), extra={"level": None})
    logger.info('Hello1', extra={"level": "INFO"})
    logger.info('"', extra={"level": "DEBUG"})
    logger.error('Hello)"', extra={"level": "ERROR"})