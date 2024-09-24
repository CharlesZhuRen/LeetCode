class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        def validIpV4(ip):
            xs = ip.split(".")

            if len(xs) != 4:
                return False

            for xi in xs:
                if not xi.isdigit():
                    return False

                if int(xi) < 0 or int(xi) > 255:
                    return False

                if xi.startswith("0") and len(xi) != 1:
                    return False

            return True

        def validIpV6(ip):
            xs = ip.split(":")

            if len(xs) != 8:
                return False

            for xi in xs:
                if len(xi) < 1 or len(xi) > 4:
                    return False

                for ch in xi:
                    if not ('a' <= ch <= 'f' or 'A' <= ch <= 'F' or '0' <= ch <= '9'):
                        return False

            return True

        if validIpV4(queryIP):
            return "IPv4"
        elif validIpV6(queryIP):
            return "IPv6"
        else:
            return "Neither"