from bs4 import BeautifulSoup

path = r'C:\Users\USER\.gemini\antigravity\brain\6c56c564-8f64-443c-b51b-e44c5b8553d7\.system_generated\steps\97\content.md'
with open(path, encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
for script in soup(["script", "style"]):
    script.extract()

text = soup.get_text(separator='\n', strip=True)
print(text[:4000])
