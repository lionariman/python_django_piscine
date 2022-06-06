import sys
import os
import re
import settings

def full_html_generate(html_piece: str):
    full_html = '''
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>myCV</title>
        </head>
        <body>
            {body}
        </body>
    </html>\n'''
    with open("myCV.html", "w") as mycv_file:
        mycv_file.write(full_html.format(body=html_piece))

def open_file_if_exists():
    if os.path.exists(sys.argv[1]) == False:
        print("There is no such file!")
        return
    with open(sys.argv[1], "r") as tm:
        html_piece = tm.read().format(
            name=settings.name,
            surname=settings.surname,
            profession=settings.profession,
            age=settings.age)
        full_html_generate(html_piece)

def main():
    if len(sys.argv) != 2:
        print("wrong number of arguments")
        return
    index = sys.argv[1].find(".template")
    word_length = len(sys.argv[1])
    if index != -1 and word_length - index == 9:
        open_file_if_exists()
    else:
        print("Wrong file extension: ", sys.argv[1])

if __name__ == "__main__":
    main()