from abc import ABCMeta, abstractmethod

class ContentProvider(metaclass=ABCMeta):
    ''' Provides content to return in a response'''

    @abstractmethod
    def getContent():
        ''' Get content. '''

        pass
