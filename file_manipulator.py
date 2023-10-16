import sys

class FileManipulator:
    def __init__(self):
        self.arg = sys.argv
        self.action = self.arg[1]
        self.inputPath = self.arg[2]
        self.outputPath = ""

    def actionControl(self):
        if self.action == "reverse":
            self.outputPath = self.arg[3]
            content = self.read(self.inputPath)[::-1]
            self.write(self.outputPath, content)

        elif self.action == "copy":
            self.outputPath = self.arg[3]
            content = self.read(self.inputPath)
            self.write(self.outputPath, content)

        elif self.action == "duplicate-contents":
            count = int(self.arg[3])
            path = self.inputPath + "_" + str(count)
            content = self.read(self.inputPath)
            content_n = ""
            for _ in range(count):
                content_n += content + "\n"
            self.write(path, content_n)

        elif self.action == "replace-string":
            needles = self.arg[2:len(self.arg) - 1]
            newString = self.arg[len(self.arg) - 1]
            content = self.read(self.inputPath)
            for needle in needles:
                content = content.replace(needle, newString)
            self.write(self.inputPath,content)
        else:
            print("コマンドが間違いています")
            sys.exit()

    def read(self, path):
        with open(path) as f:
            content = f.read()
        return content

    def write(self, path, content):
        with open(path, "w") as f:
            f.write(content)



file = FileManipulator()
file.actionControl()


