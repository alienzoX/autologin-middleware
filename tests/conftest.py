import pytest
from scrapy.crawler import CrawlerRunner


pytest_plugins = 'pytest_twisted'


def base_settings():
    return {
        'AUTOLOGIN_URL': 'http://127.0.0.1:8089',
        'AUTOLOGIN_ENABLED': True,
        # Higher fixed value to make the test more reliable
        'AUTOLOGIN_MAX_LOGOUT_COUNT': 8,
        'COOKIES_ENABLED': True,
        'COOKIES_DEBUG': True,
        'DOWNLOADER_MIDDLEWARES': {
            'autologin_middleware.AutologinMiddleware': 605,
            'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
            'autologin_middleware.ExposeCookiesMiddleware': 700,
        }
    }


@pytest.fixture(params=[False])
def settings(request):
    return base_settings()