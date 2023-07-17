# selene-py-intro/tests/test_google_search.py


from selene import browser, by, be, have































def test_google_finds_selene():

    browser.open('https://google.com/ncr')
    browser.element(by.name('q')).should(be.blank)

    browser.element(by.name('q')).type('selenidejs') \
        .press_enter()
    browser.all('#rso>div').should(have.size_greater_than_or_equal(5))
    browser.all('#rso>div').first.should(have.text('selenidejs'))

    browser.all('#rso>div').first.element('h3').click()
    browser.should(have.title_containing('GitHub - KnowledgeExpert/selenidejs'))

