#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ThemeUtils.py
#
#  Copyright © 2017 Antergos
#
#  This file is part of Web Greeter.
#
#  Web Greeter is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  Web Greeter is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  The following additional terms are in effect as per Section 7 of the license:
#
#  The preservation of all legal notices and author attributions in
#  the material or in the Appropriate Legal Notices displayed
#  by works containing it is required.
#
#  You should have received a copy of the GNU General Public License
#  along with Web Greeter; If not, see <http://www.gnu.org/licenses/>.

# Standard Lib
import os
import os.path as path

# 3rd-Party Libs
from whither.bridge import (
    BridgeObject,
    bridge,
    Variant,
)


class ThemeUtils(BridgeObject):

    def __init__(self, greeter, config, user_config, *args, **kwargs):
        super().__init__(name='ThemeUtils', *args, **kwargs)

        self._config = config
        self._user_config = user_config
        self._greeter = greeter

    @bridge.method(Variant)
    def dirlist(self, dir_path):
        if not dir_path or not isinstance(dir_path, str):
            return []

        dir_path = path.realpath(path.normpath(dir_path))

        if not path.isabs(dir_path) or not path.isdir(dir_path):
            return []

        allowed = False
        allowed_dirs = (
            self._config.themes_dir,
            self._user_config.branding.background_images,
            self._greeter.shared_data_directory,
            '/tmp/'
        )

        for allowed_dir in allowed_dirs:
            if dir_path.startswith(allowed_dir):
                allowed = True
                break

        if not allowed:
            return []

        return (path.join(dir_path, f) for f in os.listdir(dir_path))


