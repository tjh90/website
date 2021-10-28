from bs4 import BeautifulSoup

from .ContentProvider import ContentProvider

class MobileContentProvider(ContentProvider):
    ''' Provides mobile content. '''

    def __init__(self, contentProvider):
        '''
        Constructor.

        @param contentProvider the content provider instance to wrap.
        '''
        self.__contentProvider = contentProvider

    def getContent(self):
        # Get wrapped content.
        content = self.__contentProvider.getContent()

        # Parse HTML.
        parser = BeautifulSoup(content, 'html.parser')

        # Replace title content.
        parser.h1.string = parser.h1.string + ' for mobile'

        # Remove desktop-only elements.
        [tag.decompose() for tag in parser.find_all(class_='DesktopOnly')]

        return str(parser)

ContentProvider.register(MobileContentProvider)
