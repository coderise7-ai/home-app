[app]
title = Home App
package.name = homeapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 0.1
requirements = python3,kivy

[buildozer]
log_level = 2

[app]
presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png