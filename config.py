class Config:
    """The key that we'll pass in our get requests"""
    API_KEY = "a3121d3568944bf782807ac90b13b1f7"
    """This is for the base url that we'll use to make requests to the news api"""
    NEWS_API_BASE_URL = "https://newsapi.org/v2"

    pass


class DevConfig:
    DEBUG = True
    pass


class ProdConfig:
    pass
