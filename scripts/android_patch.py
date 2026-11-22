
import pathlib
import shutil

manifest = pathlib.Path("android/app/src/main/AndroidManifest.xml")
content = manifest.read_text()

permissions = [
    "ACCESS_FINE_LOCATION",
    "ACCESS_COARSE_LOCATION",
    "FOREGROUND_SERVICE",
    "FOREGROUND_SERVICE_LOCATION",
    "POST_NOTIFICATIONS",
    "WAKE_LOCK",
]

additions = "".join(
    f'    <uses-permission android:name="android.permission.{permission}" />\n'
    for permission in permissions
    if f'android.permission.{permission}"' not in content
)

manifest.write_text(content.replace("</manifest>", additions + "</manifest>"))

shutil.copytree(
    "android-overrides/res",
    "android/app/src/main/res",
    dirs_exist_ok=True
)

print("Manifesto e recursos ajustados")
