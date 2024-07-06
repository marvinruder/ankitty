<h2 align="center">Kitten Reinforcement for Anki</h2>

<p align="center">
<a title="Latest (pre-)release" href="https://github.com/marvinruder/ankitty/releases"><img src ="https://img.shields.io/github/release-pre/marvinruder/ankitty.svg?colorB=brightgreen"></a>
<a title="License: GNU AGPLv3" href="https://github.com/marvinruder/ankitty/blob/main/LICENSE"><img  src="https://img.shields.io/badge/license-GNU AGPLv3-green.svg"></a>
<a title="Rate on AnkiWeb" href="https://ankiweb.net/shared/info/1319623242"><img src="https://glutanimate.com/logos/ankiweb-rate.svg"></a>
<br>
<a title="Buy upstream maintainer a coffee :)" href="https://ko-fi.com/X8X0L4YV"><img src="https://img.shields.io/badge/ko--fi-contribute%20upstream-%23579ebd.svg"></a>
<a title="Support upstream maintainer on Patreon :D" href="https://www.patreon.com/bePatron?u=7522179"><img src="https://img.shields.io/badge/patreon-support%20upstream-%23f96854.svg"></a>
</p>

> Everything's better with kittens!

An add-on for the spaced-repetition flashcard app [Anki](https://apps.ankiweb.net/) that encourages learners with pictures of cute kittens, following the principles of intermittent positive reinforcement.

### Table of Contents <!-- omit in toc -->

<!-- MarkdownTOC levels="1,2,3" -->

- [Installation](#installation)
- [Documentation](#documentation)
- [Building](#building)
- [Contributing](#contributing)
- [License and Credits](#license-and-credits)

<!-- /MarkdownTOC -->

### Installation

#### AnkiWeb <!-- omit in toc -->

The easiest way to install Ankitty is through [AnkiWeb](https://ankiweb.net/shared/info/1319623242).

#### Manual installation <!-- omit in toc -->

1. Download the latest `.ankiaddon` file from the [releases tab](https://github.com/marvinruder/ankitty/releases) (you might need to click on *Assets* below the description to reveal the download links)
2. Open the folder where your downloads are located and double-click on the downloaded `.ankiaddon` file.
3. Follow the installation prompt and restart Anki if it asks you to

<details>

<summary><i>Alternate option</i></summary>

1. Download the latest `.ankiaddon` package from the [releases tab](https://github.com/marvinruder/ankitty/releases) (you might need to click on *Assets* below the description to reveal the download links)
2. From Anki's main window, head to *Tools* → *Add-ons*
3. Drag-and-drop the `.ankiaddon` package onto the add-ons list
4. Restart Anki

</details>

### Documentation

For further information on the use of this add-on please check out [the description text](docs/description.md) for AnkiWeb.

### Building

With [Anki add-on builder](https://github.com/glutanimate/anki-addon-builder/) installed:

    git clone https://github.com/marvinruder/ankitty.git
    cd ankitty
    aab build

For more information on the build process please refer to [`aab`'s documentation](https://github.com/glutanimate/anki-addon-builder/#usage).

### Contributing

Contributions are welcome!

### License and Credits

*Ankitty*, a fork of *[Puppy Reinforcement](https://github.com/glutanimate/puppy-reinforcement)*, is *Copyright © 2024 [Marvin A. Ruder](https://github.com/marvinruder) (marvinruder)*

*Puppy Reinforcement* is *Copyright © 2016-2023 [Aristotelis P.](https://glutanimate.com/) (Glutanimate)*

With code contributions from: [@zjosua](https://github.com/zjosua) (thanks!)

Ankitty is free and open-source software. The add-on code that runs within Anki is released under the GNU AGPLv3 license, extended by a number of additional terms. For more information please see the [LICENSE](https://github.com/marvinruder/ankitty/blob/main/LICENSE) file that accompanied this program.

Please note that this program uses the [Libaddon](https://github.com/glutanimate/anki-libaddon/) library which comes with [its own additional terms extending the GNU AGPLv3 license](https://github.com/marvinruder/ankitty/blob/main/src/puppy_reinforcement/libaddon/LICENSE). You may only copy, distribute, or modify the present compilation of this program with Libaddon under the combined licensing terms specified by both licenses.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.

----

<b>
<div align="center">The continued development of this add-on is made possible <br>thanks to the upstream maintainer’s <a href="https://www.patreon.com/glutanimate">Patreon</a>  supporters.</div>
</b>
