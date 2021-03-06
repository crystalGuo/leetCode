import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return False

        intNumber = "(([0-9])|([1-9][0-9]+))"
        dotNumber = "([.][0-9]+)"
        sign = "[+-]?"
        floatwithoute = sign + "((" + dotNumber + ")|(" + intNumber + '.' + ")|(" + intNumber + dotNumber + "?" + "))"
        WS = "[ ]*"

        result = re.match("^" + WS + floatwithoute + '([e]' + sign + intNumber + ")?" + WS + "$", s)
        return not (result is None)
