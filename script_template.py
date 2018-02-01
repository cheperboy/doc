import os, sys, argparse
import logging, logging.config
#ADD import serial

PORT = '/dev/ttyS0'
BAUDRATE = 1200
#ADD 
STOPBITS = "serial.STOPBITS_ONE"
BYTESIZE = "serial.SEVENBITS"


# Gather our code in a main() function
def main():

    # TODO Replace this with your actual code.
    print "Hello there."
    logging.critical(os.path.basename(__file__))
    logging.error("ERROR")
    logging.warning("WARNING")
    logging.info("INFO")
    logging.debug("DEBUG")
 
 

if __name__ == '__main__':
    #filename of this script
    script_name = os.path.basename(__file__)
    
    parser = argparse.ArgumentParser(description = "Rpi gets teleinfo from EDF serial output", epilog = "" )
    parser.add_argument("-v",
                          "--verbose",
                          help="increase output verbosity",
                          action="store_true")
    args = parser.parse_args()

    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.CRITICAL
    
    logger = logging.getLogger(__name__)
    logging.config.dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(asctime)s | %(name)s | %(filename)s | %(funcName)s | %(levelname)s | %(message)s"
            }
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": loglevel,
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            },

            "info_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "simple",
                "filename": "log/" + script_name + "_info.log",
                "maxBytes": 100000,
                "backupCount": 3,
                "encoding": "utf8"
            },

            "error_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "simple",
                "filename": "log/" + script_name + "_errors.log",
                "maxBytes": 100000,
                "backupCount": 3,
                "encoding": "utf8"
            }
        },

        "loggers": {
            "my_module": {
                "level": "ERROR",
                "handlers": ["console"],
                "propagate": "no"
            }
        },

        "root": {
            "level": "INFO",
            "handlers": ["console", "info_file_handler", "error_file_handler"]
        }
    })

    main()
