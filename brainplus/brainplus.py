"Main module"
import sys

C_INTRO = """
#include <stdio.h>

int main(void) {
long memory[30000];
long *p = memory;
int *temp;

"""


def cname(s):
    "Returns the C source file name for a given Brainfuck file."
    return s.split('.')[0] + ".c"


def main(argv=None):
    "Main function"
    source = ''
    if argv is None:
        argv = sys.argv
    if len(argv) < 2:
        sys.stderr.write("brainplus: too few arguments. Usage: python -m brainplus FILE") # noqa
        sys.exit(1)
    with open(argv[1], "r", encoding="utf-8") as fin:
        source = fin.read()
    with open(cname(argv[1]), "w", encoding="utf-8") as fout:
        fout.write(C_INTRO)
        for char in source:
            match char:
                case "<":
                    fout.write("p--;\n")
                case ">":
                    fout.write("p++;\n")
                case "+":
                    fout.write("(*p)++;\n")
                case "-":
                    fout.write("(*p)--;\n")
                case ".":
                    fout.write("putchar(*p);\n")
                case ",":
                    fout.write("*p = getchar();\n")
                case "&":
                    fout.write("temp = &memory[(*p)+1]; p = temp;\n")
                case "a":
                    fout.write("*p += *(p+1);\n")
                case "s":
                    fout.write("*p -= *(p+1);\n")
                case "m":
                    fout.write("*p *= *(p+1);\n")
                case ";":
                    fout.write('scanf("%ld", p);\n')
                case ":":
                    fout.write('printf("%ld", (*p));\n')
        fout.write("\n}\n")
