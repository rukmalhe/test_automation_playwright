class DuckDuckGoSearchPage:
    def __init__(self, page):
        self.page = page
        self.search_input = page.locator('input[name="q"]')  # Adjust selector as necessary
        self.search_button = page.locator('button[type="submit"]')

    def load(self):
        self.page.goto('https://duckduckgo.com')

    def search(self, phrase: str):
        self.search_input.fill(phrase)
        self.search_button.click()
