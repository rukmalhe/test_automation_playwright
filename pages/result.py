class DuckDuckGoResultPage:
    def __init__(self, page):
        self.page = page
        self.search_input = page.locator('input[name="q"]')
        self.result_links = page.locator('a.result__a')

    def result_link_titles_contain_phrase(self, phrase: str) -> bool:
        # Checking that result links contain the phrase
        titles = self.result_links.all_text_contents()
        return all(phrase.lower() in title.lower() for title in titles)
