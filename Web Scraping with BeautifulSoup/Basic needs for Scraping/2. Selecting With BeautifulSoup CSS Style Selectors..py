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
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# Select with Css selector
# select always return as a List !
# You can use select_one instead of select - if you want one item back
# select with CSS - has a much more cleaner syntax !
print(soup.select_one("#first"))
print(soup.select(".special"))
print(soup.select_one("div"))
print(soup.select_one("ol"))
print(soup.select("ol li "))
print(soup.select_one("[data-example]"))    # <h3 data-example="yes">hi</h3>
print(soup.select("[data-example]"))  # [<h3 data-example="yes">hi</h3>, <div data-example="yes">bye</div>]
