# !/usr/bin/env python
# -*- coding: utf-8 -*-

from views import console, append_feedback, create_feedback

if __name__ == '__main__':
    create_fb = create_feedback.CreateFb()
    append_fb = append_feedback.AppendFb()
    console = console.Console()

    create_fb.start_create()
    append_fb.start_append()
    console.console()
