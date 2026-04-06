from copier import copier
from generate_page import generate_page
import sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copier("static", "docs")
    generate_page("content", "template.html", "docs", basepath)

main() 