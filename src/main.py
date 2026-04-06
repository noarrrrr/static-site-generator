from copier import copier
from generate_page import generate_page

def main():
    copier("static", "public")
    generate_page("content", "template.html", "public")

main() 