# -*- coding: utf-8 -*-

# Kitten Reinforcement Add-on for Anki
#
# Copyright (C) 2016-2023  Aristotelis P. <https://glutanimate.com/>
# Copyright (C) 2024       Marvin A. Ruder <https://github.com/marvinruder>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the license file that accompanied this program.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License that
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://github.com/marvinruder>.
#
# Any modifications to this file must keep this entire header intact.

"""
Addon-wide constants
"""

from ._version import __version__

__all__ = ["ADDON"]

# PROPERTIES DESCRIBING ADDON

class ADDON:
    """Class storing general add-on properties
    Property names need to be all-uppercase with no leading underscores
    """

    NAME = "Ankitty"
    MODULE = "ankitty"
    ID = "1319623242"
    VERSION = __version__
    LICENSE = "GNU AGPLv3"
    AUTHORS = (
        {
            "name": "Marvin A. Ruder (marvinruder)",
            "years": "2024",
            "contact": "https://github.com/marvinruder",
        },
    )
    AUTHOR_MAIL = "ankitty@mruder.dev"
    LIBRARIES = ()
    CONTRIBUTORS = ("glutanimate", "zjosua",)
    SPONSORS = ()
    LINKS = {
        "patreon": "https://www.patreon.com/glutanimate",
        "bepatron": "https://www.patreon.com/bePatron?u=7522179",
        "coffee": "http://ko-fi.com/glutanimate",
        "description": "https://ankiweb.net/shared/info/{}".format(ID),
        "rate": "https://ankiweb.net/shared/review/{}".format(ID),
        "twitter": "",
        "youtube": "",
        "help": "",
    }
