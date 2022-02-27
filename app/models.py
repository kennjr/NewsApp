class newsSource:

    def __init__(self, source_id, source_name):
        self.source_id = source_id
        self.source_name = source_name


class newsArticle:
    def __init__(self, description, source, author, title, url, url_to_image, published_at, content):
        self.description = description
        self.title = title
        self.source = source
        self.author = author
        self.url = url
        self.url_to_image = url_to_image
        self.published_at = published_at
        self.content = content
