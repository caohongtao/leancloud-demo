from leancloud import Object

class Logger(Object):

    @classmethod
    def println(cls, content):
        info = cls()
        info.set('content', content)
        info.save()