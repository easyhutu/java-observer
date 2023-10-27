from javaObserver import utils


class JavaFile:
    def __init__(self, path):
        self.path = path
        self._fileSize = None

    @property
    def fileSize(self):
        """文件大小，单位KB"""
        if self._fileSize:
            return self._fileSize
        return utils.roundSize(len(self.content) / 1024)

    @property
    def content(self):
        """文件内容"""
        with open(self.path, encoding='u8') as f:
            content = f.read()
            self._fileSize = utils.roundSize(len(content) / 1024)
            return content
