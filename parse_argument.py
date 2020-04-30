import argparse
import os

parser = argparse.ArgumentParser(description="Music sorter program")
parser.add_argument('-s', '--src-dir',
                    type=str,
                    default=os.getcwd(),
                    help='исходная директория, по умолчанию директория в которой запущен скрипт;'
                    )
parser.add_argument('-d', '--dst-dir',
                    type=str,
                    default=os.getcwd(),
                    help='целевая директория, по умолчанию директория в которой запущен скрипт'
                    )
parse_arguments = parser.parse_args()
