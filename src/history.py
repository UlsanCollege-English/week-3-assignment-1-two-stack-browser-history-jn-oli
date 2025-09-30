# src/history.py

class BrowserHistory:
    def __init__(self):
        self._current = "home"
        self._back_stack = []
        self._forward_stack = []

    def current(self):
        return self._current

    def visit(self, url: str):
        if self._current != "home":      # only push real pages
            self._back_stack.append(self._current)
        self._current = url
        self._forward_stack.clear()

    def back(self):
        if not self._back_stack:
            raise IndexError("No pages in back history")
        self._forward_stack.append(self._current)
        self._current = self._back_stack.pop()
        return self._current

    def forward(self):
        if not self._forward_stack:
            raise IndexError("No pages in forward history")
        self._back_stack.append(self._current)
        self._current = self._forward_stack.pop()
        return self._current
