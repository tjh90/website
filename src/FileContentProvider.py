from .ContentProvider import ContentProvider

class FileContentProvider(ContentProvider):
    ''' Provide content from a file. '''

    def __init__(self, filename):
        '''
        Constructor

        @param filename the name of the file to read and use as the response.
        '''

        self.__filename = filename

    def getContent(self):
        with open(self.__filename, 'r') as file:
            return file.read()

ContentProvider.register(FileContentProvider)
