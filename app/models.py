class newsSource:
    def __init__(self, source_id, source_name, source_img, source_description, source_url):
        self.source_id = source_id
        self.source_name = source_name
        self.source_img = source_img
        self.source_description = source_description
        self.source_url = source_url


class newsArticle:
    """The custom_url is for the url that we create for the """
    def __init__(self, description, source, author, title, url, url_to_image, published_at, content, custom_url):
        self.description = description
        self.title = title
        self.source = source
        self.author = author
        self.url = url
        self.url_to_image = url_to_image
        self.published_at = published_at
        self.content = content
        self.custom_url = custom_url
