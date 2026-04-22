[app]
title = FACTURrrr
package.name = facturrrr
package.domain = org.vtlo

# Source code
source.dir = .
source.include_exts = py,png,jpg,j2,html,txt,css,js
source.include_patterns = templates/*,static/*

# Dépendances (Adapté à Factur-X et Flask)
requirements = python3,flask,jinja2,werkzeug,itsdangerous,click,facturx,pypdf,lxml

version = 0.1
orientation = portrait
fullscreen = 0

# Permissions Android (Nécessaire pour sauvegarder les factures PDF)
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Architecture
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
