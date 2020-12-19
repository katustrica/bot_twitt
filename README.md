# bot_twitt
python bot.py

### Localization

In bot_twitt gettext is used for localization. To update localization
it is required to install gettext from off-site.

To update `.pot` files:
```
dir /S /B *.py > pyfiles
C:\Users\gtr42\WorkFolder\GnuWin32\bin\xgettext.exe -p locale -o bot_twitt.pot --from-code UTF-8 -L Python -f pyfiles
```

To update `.po` files from `.pot` with saving of previous translations use `msgmerge`:
```
C:\Users\gtr42\WorkFolder\GnuWin32\bin\msgmerge.exe -o locale\en\LC_MESSAGES\bot_twitt.po locale\en\LC_MESSAGES\bot_twitt.po locale\bot_twitt.pot
C:\Users\gtr42\WorkFolder\GnuWin32\bin\msgmerge.exe -o locale\ru\LC_MESSAGES\bot_twitt.po locale\ru\LC_MESSAGES\bot_twitt.po locale\bot_twitt.pot
```

To edit messages poedit is recommended. But you can also update
localization it `.po` files directly.

To compile update `.po`-files use command `msgfmt`:
```
C:\Users\gtr42\WorkFolder\GnuWin32\bin\msgfmt.exe -o locale\en\LC_MESSAGES\bot_twitt.mo locale\en\LC_MESSAGES\bot_twitt.po
C:\Users\gtr42\WorkFolder\GnuWin32\bin\msgfmt.exe -o locale\ru\LC_MESSAGES\bot_twitt.mo locale\ru\LC_MESSAGES\bot_twitt.po
```
