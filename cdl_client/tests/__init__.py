# -*- coding: utf-8 -*-
#
# Licensed under the terms of the BSD 3-Clause
# (see cdl_client/LICENSE for details)

"""
CDL_Client unit tests
"""

from __future__ import annotations

from guidata.guitest import run_testlauncher

import cdl_client


def run() -> None:
    """Run DataLab test launcher"""
    run_testlauncher(cdl_client)


if __name__ == "__main__":
    run()
