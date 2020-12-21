import markdown

markdown.markdownFromFile(
    input='README.md', output='output.html', encoding='utf-8', extensions=['fenced_code', 'codehilite']
)
