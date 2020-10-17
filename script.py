import os
import argparse
from helpers import utils


# global vars
#############
logger = args = None
#############


def empty_output_file(output='.output'):
    with open(output, "w") as outfile: pass
    logger.info('Output file {} has been created and emptied...'.format(output))
    return output


def setup_args():
    parser = argparse.ArgumentParser(os.path.basename(__file__))
    parser.add_argument('-v', '--verbosity', metavar='<verbosity_level>', type=str, default='DEBUG', help='Execution verbosity level. Eg: SUCCESS|WARN|INFO|DEBUG.')
    logger.info('Arguments parsed successfully...')
    return parser.parse_args()


def initialize_g_vars():
    global logger, args
    logger = utils.setup_logger()
    args = setup_args()
    if args.verbosity is not None and not args.verbosity: logger.setLevel(args.verbosity)
    logger.info('initialize_g_vars() finished successfully...')

    
def main():
    try:
        initialize_g_vars()
        empty_output_file(output=args.output)
    except Exception as e:
        logger.error('Exception {} occurred in main of file {}...'.format(e, os.path.basename(__file__)))


###### main execution ######
if __name__ == '__main__':
    main()
############################
