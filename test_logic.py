from mylib.logic import wiki, search_wiki


def test_wiki():
    assert "god" in wiki()


def test_search_wiki():
    assert 'Amin' in search_wiki('Amin')
