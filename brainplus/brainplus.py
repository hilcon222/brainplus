"Main module"
import sys

C_INTRO = """
#include <stdio.h>

int main(void) {
long memory[30000];

"""


def cname(source):
    "Returns the C source file name for a given Brainfuck file."
    return source.split('.')[0] + ".c"


def main(argv=None):
    "Main function"
    if argv is None:
        argv = sys.argv
    if len(argv) < 2:
        sys.stderr.write("brainplus: too few arguments. Usage: python -m brainplus FILE") # noqa
        sys.exit(1)
    with open(cname(argv[1]), "w", encoding="utf-8") as fout:
        fout.write(C_INTRO)
