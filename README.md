# Web Greeter for LightDM
[![Latest Release][release]](https://github.com/Antergos/web-greeter/releases)  &nbsp;[![Codacy Grade][codacy]](https://www.codacy.com/app/Antergos/web-greeter) &nbsp;[![CircleCI][circleci]](https://circleci.com/gh/Antergos/web-greeter) &nbsp;[![Theme API Docs][api]](https://doclets.io/Antergos/web-greeter/stable) &nbsp;[![AUR Votes][aur]](https://aur.archlinux.org/packages/lightdm-webkit2-greeter)

## Install It

### Distro Packages
|Distro|Install Command/Links|
|:---:|:---:|
|![antergos][antergos]|`sudo pacman -S lightdm-webkit2-greeter`|
|![arch][arch]        |`yaourt -S lightdm-webkit2-greeter`|
|![fedora][fedora]    |`dnf copr enable antergos/lightdm-webkit2-greeter`|
|![openSUSE][openSUSE]|[1 Click Install](https://software.opensuse.org/ymp/home:antergos/openSUSE_Leap_42.2/lightdm-webkit2-greeter.ymp?base=openSUSE%3ALeap%3A42.2&query=lightdm-webkit2-greeter)|
|![ubuntu][ubuntu]    |[OBS Repo](https://software.opensuse.org/download.html?project=home:antergos&package=lightdm-webkit2-greeter)|

### From Source

#### Dependencies
|                       | ![antergos][antergos] &nbsp;&nbsp; ![arch][arch] | ![ubuntu][ubuntu]    | ![fedora][fedora]   | ![openSUSE][openSUSE] | 
|-----------------------|--------------------------------------------------|----------------------|---------------------|-----------------------|
|**[whither][whither]** |python-whither                                    |python3-whither       |python3-whither      |python3-whither        |
|**liblightdm-gobject** |lightdm                                           |liblightdm-gobject-dev|lightdm-gobject-devel|liblightdm-gobject-1-0 |
|**pygobject**          |python-gobject                                    |python3-gi            |pygobject3           |python3-gobject        |

> ***NOTE:*** These instructions are for the `master` branch. To build the latest release, please see the `stable` branch.

#### Download & Install
```sh
git clone https://github.com/Antergos/web-greeter.git /tmp/greeter
cd /tmp/greeter
sudo make install
```

## Theme JavaScript API
The greeter exposes a JavaScript API to themes which they must use to interact with the greeter (in order to facilitate the user login process). For more details, check out the [API Documentation](https://doclets.io/Antergos/web-greeter/stable). 

## Debugging
You can run the greeter from within your desktop session if you add the following line to the desktop file for your session located in `/usr/share/xsessions/`: `X-LightDM-Allow-Greeter=true`.

You have to log out and log back in after adding that line. Then you can run the greeter from command line.

```sh
web-greeter
```

Themes can be opened with a debug console if you set `debug_mode` to `true` inside `/etc/lightdm/web-greeter.yml`.

> ***Note:*** Do not use `lightdm --test-mode` as it is not supported.

## Translations
Translations are managed through [Transifex](https://www.transifex.com/faidoc/antergos/lightdm-webkit2-greeter/).


[antergos]: https://www.dropbox.com/s/tju7maccr328w87/logo-square26x26.png?dl=1 "antergos"
[arch]: https://www.dropbox.com/s/q8ypd345cqcd0b5/archlogo26x26.png?dl=1 "arch"
[fedora]: https://www.dropbox.com/s/b8q448vuwopb0cl/fedora-logo.png?dl=1 "fedora"
[openSUSE]: https://www.dropbox.com/s/jhirpw85ztgl59h/Geeko-button-bling7.png?dl=1 "openSUSE"
[ubuntu]: https://www.dropbox.com/s/nev98nld2u1qbgl/ubuntu_orange_hex.png?dl=1 "ubuntu"

[release]: https://img.shields.io/github/release/Antergos/web-greeter.svg?style=flat-square "Latest Release"
[codacy]: https://img.shields.io/codacy/grade/43c95c8c0e3749b8afa3bfd2b6edf541.svg?style=flat-square "Codacy Grade"
[circleci]: https://img.shields.io/circleci/project/Antergos/web-greeter/master.svg?style=flat-square "CI Status"
[api]: https://img.shields.io/badge/API--Docs-ready-brightgreen.svg?style=flat-square "Theme API Docs"
[aur]: https://img.shields.io/aur/votes/lightdm-webkit2-greeter.svg?maxAge=604800&style=flat-square "AUR Votes"

[whither]: https://github.com/Antergos/whither "Whither"
