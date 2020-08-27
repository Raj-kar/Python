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
print(soup.body)
print(soup.find("div"))
print(soup.find_all("div"))
print(soup.body.h3)
print(soup.body.ol)
print(soup.body.ol.find_all("li"))
print(soup.find(id="first"))
print(soup.findChild("ol"))
print(soup.find_all(class_="special"))
print(soup.find(attrs={"data-example": "yes"}))
