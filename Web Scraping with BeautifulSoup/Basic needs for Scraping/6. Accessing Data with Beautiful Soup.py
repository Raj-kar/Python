from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special super-special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print(soup.select_one("li").get_text())

for data in soup.select("li"):
    print(data.get_text())

print(soup.find("div")["id"])

print(soup.select_one(".special").name)

for data in soup.select("li"):
    print(data.attrs)
    # Both are same[above one access with css and below one select with tag]
for data in soup.find_all(class_="special"):
    print(data.attrs)
