from distutils.core import setup
import py2exe

setup(
    windows=[
        {
            "script": "main.py",
            "icon_resources": [(1, "invoice\\gui\\image\\main_logo.ico")]
        }],
    options={
        "py2exe":
            {
                "includes": ["sip"],
                "packages": ["sqlalchemy"]
            }
    })
