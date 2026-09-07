class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join([c.lower() if c.upper() else c for c in s])