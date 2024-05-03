from io import StringIO


class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        str_enc = StringIO()
        for s in strs:
            str_enc.write(str(len(s)))
            str_enc.write(">")
            str_enc.write(s)

        return str_enc.getvalue()

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        strs: list[str] = []

        p1 = 0
        while p1 < len(s):
            p2 = p1
            while s[p1] != ">":
                p1 += 1

            len_s = int(s[p2:p1])
            p2 = p1 + 1
            p1 += 1 + len_s

            strs.append(s[p2:p1])

        return strs


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
