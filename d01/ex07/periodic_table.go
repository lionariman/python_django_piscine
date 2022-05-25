package main

import (
	"fmt"
	"os"
	"strings"
	"strconv"
)

func check(e error, msg string) {
	if e != nil {
		fmt.Println("ERROR: ", e, "\n|", msg, "|")
		os.Exit(2)
	}
}

func skipTableCells(pos int, position int) (body string) {
	counter := position - pos
	if pos >= position {
		counter = pos - position
	}
	for i := 0; i < counter - 1; i++ {
		body += "<td></td>\n"
	}
	return
}

func getTableBody(key string, values []string) (body string) {
	body = fmt.Sprintf(`
	<td class="cell">
        <h4>%s</h4>
        <ul>
            <li>No %s</li>
            <li>%s</li>
            <li>%s</li>
            <li>%s electron</li>
        </ul>
    </td>
	`,
		strings.TrimSpace(key),
		strings.TrimSpace(strings.Split(values[1], ":")[1]),
		strings.TrimSpace(strings.Split(values[2], ":")[1]),
		strings.TrimSpace(strings.Split(values[3], ":")[1]),
		strings.TrimSpace(strings.Split(values[4], ":")[1]),
	)
	return
}

func getMainHtmlPage(body string) (html string) {
	html = fmt.Sprintf(`
    <!DOCTYPE html>
    <html>
        <head>
            <title>Periodic Table</title>
            <link href="periodic_table.css" rel="stylesheet">
        </head>
        <body>
            <h1>Periodic Table</h1>
            <table>
                %s
            </table>
        </body>
    </html>
    `,
	body)
	return
}

func generateCssFile() (css string) {
	css = `
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
        box-shadow: -5px 5px 10px1 #999999,
                    5px -5px 10px #ffffff;
    }

    .cell:hover {
        background: linear-gradient(225deg, #e6e6e6, #ffffff);
        box-shadow: -5px 5px 10px #999999,
                    5px -5px 10px #ffffff;
    }
	`
	err := os.WriteFile("periodic_table.css", []byte(css), 0644)
	check(err, "not able to write to CSS file")
	return
}

func main() {
	fileTxt, err := os.ReadFile("periodic_table.txt")
	check(err, "not able to open the file")

	lines := strings.Split(string(fileTxt), "\n")

	body := "<tr>"
	pos := 0
	for i := 0; i < len(lines) - 1; i++ {
		items := strings.Split(lines[i], "=")
		key := items[0]
		values := strings.Split(items[1], ", ")
		position, err := strconv.Atoi(strings.Split(values[0], ":")[1])
		check(err, "not able to find a position")
		if position == 17 {
			body += skipTableCells(pos, position)
			body += getTableBody(key, values)
			body += "</tr>\n<tr>\n"
			position = 0
		} else {
			body += skipTableCells(pos, position)
			body += getTableBody(key, values)
		}
		pos = position
	}
	body += "</tr>\n"
	err = os.WriteFile("periodic_table.html", []byte(getMainHtmlPage(body)), 0644)
	check(err, "not able to write to HTML file")
	generateCssFile()
}