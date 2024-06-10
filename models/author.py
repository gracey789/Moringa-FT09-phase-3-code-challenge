from database.connection import get_db_connection
class Author:
    def _init_(self, id, name):
        self._id = id
        self.name = name

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        if not hasattr(self, '_name'):
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT name FROM authors WHERE id = ?', (self._id,))
            result = cursor.fetchone()
            if result:
                self._name = result[0]
            else:
                raise ValueError("Name not found in database")
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = value
    
    def articles(self):
        from models.article import Article
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE author_id = ?', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return [Article(article['id'], article['title'], article['content'], article['author_id'], article['magazine_id']) for article in articles]
    
    
    def magazines(self):
        from models.magazine import Magazine
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT magazines. * FROM magazines
            INNER JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.author_id = ?
        ''', (self._id,))
        magazines = cursor.fetchall()
        conn.close()
        return [Magazine(magazine['id'], magazine['name'], magazine['category']) for magazine in magazines]

    def _repr_(self):
        return f'<Author {self.name}>'