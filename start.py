# -*- coding: utf-8 -*-
"""
CERMMorse : start
5/12/2017 : 3:46 PM
Author : James L. Key

Loads the main function from morse as a daemon
This seems to only work in *nix
requires python-daemon-3k module
"""
import os
if os != 'nt':
    import daemon

    from CERMMorse import CERMMorse

    with daemon.DaemonContext():
        CERMMorse.main()
