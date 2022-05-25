def get_table_body(key, values):
    table_body = '''
    <td class="cell">
        <h4>{name}</h4>
        <ul>
            <li>No {number}</li>
            <li>{small}</li>
            <li>{molar}</li>
            <li>{electron} electron</li>
        </ul>
    </td>
    '''
    return table_body.format(
        name = key.strip(),
        number = values[1].split(":")[1].strip(),
        small = values[2].split(":")[1].strip(),
        molar = values[3].split(":")[1].strip(),
        electron = values[4].split(":")[1].strip()
    )

def get_main_html_page(body):
    html = '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Periodic Table</title>
            <link href="periodic_table.css" rel="stylesheet"
        </head>
        <body>
            <h1>Periodic Table</h1>
            <table>
                {body}
            </table>
        </body>
    </html>
    '''
    return html.format(body=body)

def skip_table_cells(pos, position):
    body = ""
    counter = position - pos
    if pos >= position:
        counter = pos - position
    i = 0
    while i < counter - 1:
        body += "<td></td>\n"
        i += 1
    return body

def generate_css_file():
    css = '''
    html {
        box-sizing: border-box;
        font-size: 12px;
    }

    body {
        font-family: "Roboto Mono", monospace;
        margin: 0;
        background-color: var(--background-color);
        color: var(--base-text-color);
    }

    table {
        border-spacing: 0.5rem;
    }

    .cell {
        border: 0px solid rgb(255, 255, 255);
        padding:10px;
        background: linear-gradient(225deg, #ffffff, #e6e6e6);
        box-shadow: -5px 5px 10px #999999,
                    5px -5px 10px #ffffff;
    }

    .cell:hover {
        background: linear-gradient(225deg, #e6e6e6, #ffffff);
        box-shadow: -5px 5px 10px #999999,
                    5px -5px 10px #ffffff;
    }

    '''
    with open("periodic_table.css", "w") as file_css:
        file_css.write(css)

def main():
    body = "<tr>"
    with open("periodic_table.txt", "r") as file_txt:
        line = file_txt.readline()
        pos = 0
        while line:
            items = line.split("=")
            key = items[0]
            values = items[1].split(", ")
            position = int(values[0].split(":")[1])
            if position == 17:
                body += skip_table_cells(pos, position)
                body += get_table_body(key, values)
                body += "</tr>\n<tr>\n"
                position = 0
            else:
                body += skip_table_cells(pos, position)
                body += get_table_body(key, values)
            line = file_txt.readline()
            pos = position
        body += "</tr>\n"
    with open("periodic_table.html", "w") as file_html:
        file_html.write(get_main_html_page(body))
    generate_css_file()


if __name__ == "__main__":
    main()