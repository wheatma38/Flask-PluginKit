# -*- coding: utf-8 -*-

version = "1.2.0"

author = "staugur"

email = "staugur@saintic.com"

from .exceptions import PluginError, TarError, ZipError, InstallError, CSSLoadError
from .flask_pluginkit import PluginManager
from .installer import PluginInstaller
from .web import blueprint
from .fixflask import Flask

__all__ = ["Flask", "PluginManager", "PluginInstaller", "blueprint", "PluginError", "TarError", "ZipError", "InstallError", "CSSLoadError"]
