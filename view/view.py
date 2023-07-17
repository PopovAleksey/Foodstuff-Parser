import os


class View:
    COLOR_DEFAULT: str = '\033[0m'
    COLOR_PURPLE: str = '\033[0;35m'
    COLOR_YELLOW: str = '\033[1;33m'
    COLOR_CYAN: str = '\033[0;36m'
    COLOR_RED: str = '\033[0;31m'
    COLOR_L_GREEN: str = '\033[1;32m'

    def showBanner(self):
        print(
            "\n\t _______                 __ ______\n" +
            "\t|    ___|.-----.-----.--|  |   __ \\.---.-.----.-----.-----.----.\t%sv%s%s\n" %
            (self.COLOR_YELLOW, os.getenv('VERSION'), self.COLOR_DEFAULT) +
            "\t|    ___||  _  |  _  |  _  |    __/|  _  |   _|__ --|  -__|   _|\n" +
            "\t|___|    |_____|_____|_____|___|   |___._|__| |_____|_____|__|\n"
        )
        print("\t\t%sAuthor:\t%s%s" % (self.COLOR_PURPLE, self.COLOR_DEFAULT, os.getenv('AUTHOR_NAME')))
        print("\t\t%sE-mail:\t%s%s" % (self.COLOR_PURPLE, self.COLOR_DEFAULT, os.getenv('AUTHOR_EMAIL')))

    def showMenu(self):
        print("\n\t\t%s[%s1%s]\t%sRun parser from start" % (self.COLOR_RED, self.COLOR_YELLOW, self.COLOR_RED, self.COLOR_CYAN))
        print("\t\t%s[%s2%s]\t%sRun parser from last stopped point" % (self.COLOR_RED, self.COLOR_YELLOW, self.COLOR_RED, self.COLOR_CYAN))
        print("\t\t%s[%s3%s]\t%sRefresh database" % (self.COLOR_RED, self.COLOR_YELLOW, self.COLOR_RED, self.COLOR_CYAN))
        print(self.COLOR_DEFAULT)

    def proposeChoose(self) -> str:
        return input("\t\t%sChoose menu number: " % self.COLOR_L_GREEN)

    def separator(self):
        print("%s-" % self.COLOR_DEFAULT * 100)