# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module manages the application (used the packages)."""

from views import console, append_fb, create_fb

if __name__ == '__main__':
    create_fb = create_fb.CreateFb()
    append_fb = append_fb.AppendFb()
    console = console.Console()

    create_fb.start_create()
    append_fb.start_append()
    console.console()
