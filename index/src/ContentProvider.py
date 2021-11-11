from abc import ABCMeta, abstractmethod

class ContentProvider(metaclass=ABCMeta):
    ''' Provides content to return in a response. '''

    @abstractmethod
    def getContent():
        '''
        Get content to use as response body.

        @returns the response body to use.
        '''

        pass
