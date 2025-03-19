
from datetime import datetime
import logging
import os


def file_output(txt:list):
    """ Write the output to a file in the output/ directory """
    directory = 'output'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # write the output to a file
    date_label = datetime.now().strftime("%Y-%m-%d-%H-%M")
    with open(f'output/{date_label}.txt', 'w') as f:
        f.writelines(txt)
    logging.info(f"Output written to output/{date_label}.txt")