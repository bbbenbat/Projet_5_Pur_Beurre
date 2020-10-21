# !/usr/bin/env python
# -*- coding: utf-8 -*-

from views import console, append_feedback
from admin import append

if __name__ == '__main__':
    console = console.Console()
    append_fb = append_feedback.Append_fb()
    api = append.Api()

    append_fb.start_append()
    console.console()
