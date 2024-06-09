import os

def defineNextPagePath(directory="./pages"):
  return f"pages/page{int(os.listdir(directory)[0][-5])+1}.htm"

theme = input("Theme: ")
words = []
while True:
    i = input()
    if i: words.append(f"        <li>{i}</li>")
    else: break

html = f'''<!DOCTYPE html>
<html>
<head>
    <title>{theme}</title>
</head>
<body>
    <h1>{theme}</h1>
    <ul>
{'\n'.join(words)}
    </ul>
    <a href="../index.htm">Back to Home</a>
</body>
</html>'''

with open(defineNextPagePath(), "w") as page_file:
    page_file.write(html)

with open("index.htm", "r") as home_file:
    home_html = home_file.read()
    with open("index.htm", "w") as home_file:
        new_li_element = f'<li><a href="{defineNextPagePath()}">{theme}</a></li>\n'
        closing_ul_tag_index = home_html.rfind("</ul>")
        modified_html = home_html[:closing_ul_tag_index] + new_li_element + home_html[closing_ul_tag_index:]
        home_file.write(modified_html)
        print(modified_html)
print("==================================")
print(html)
