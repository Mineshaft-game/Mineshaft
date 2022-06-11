import os
import i18n

global assets_dir
i18n.set("file_format", "json")
i18n.set("filename_format", "{locale}.{format}")

i18n.set("locale", os.getenv("LANG"))
i18n.set("fallback", "en")
