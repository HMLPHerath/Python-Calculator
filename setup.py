from cx_Freeze import setup, Executable
import sys  # Import sys module

includefiles=['icon.ico']
excludes=[]
packages=[]
base=None
if sys.platform=="win32":
    base="Win32GUI"

shortcut_table=[
    ("DesktopShortcut",
     "DesktopFolder",
     "Simple Calculator",
     "TARGETDIR",
     "[TARGETDIR]\Calculator.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data={"Shortcut":shortcut_table}

bdist_msi_options={'data':msi_data}
setup(
    version="0.1",
    description="Simple Calculator",
    author="Lahiru Praboth",
    name="Simple Calculator",
    options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="Calculator.py",
            base=base,
            icon='icon.ico',
        )
    ]
)

