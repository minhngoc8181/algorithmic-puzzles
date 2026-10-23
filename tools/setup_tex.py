"""Install/update shared MiKTeX for the current Windows user, not per project."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def run(*arguments, capture=False):
    return subprocess.run(list(map(str, arguments)), check=True, text=True,
                          encoding="utf-8", errors="replace",
                          stdout=subprocess.PIPE if capture else None,
                          stderr=subprocess.STDOUT if capture else None)


def add_user_path(directory):
    """Append an existing directory, preserving the user's PATH and its type."""
    import winreg
    directory = str(directory)
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0,
                        winreg.KEY_READ | winreg.KEY_SET_VALUE) as key:
        try:
            value, kind = winreg.QueryValueEx(key, "Path")
        except FileNotFoundError:
            value, kind = "", winreg.REG_EXPAND_SZ
        normalized = {os.path.normcase(os.path.expandvars(p).rstrip("\\/")) for p in value.split(";")}
        if os.path.normcase(directory.rstrip("\\/")) not in normalized:
            winreg.SetValueEx(key, "Path", 0, kind, value.rstrip(";") + ";" + directory)
    if directory not in os.environ.get("PATH", "").split(os.pathsep):
        os.environ["PATH"] = os.environ.get("PATH", "") + os.pathsep + directory


def notify_environment_change():
    """Let Explorer refresh its environment for newly launched applications."""
    import ctypes
    result = ctypes.c_size_t()
    ctypes.windll.user32.SendMessageTimeoutW(0xffff, 0x001a, 0,
                                            ctypes.c_wchar_p("Environment"),
                                            0x0002, 1000, ctypes.byref(result))


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if os.name != "nt":
        raise SystemExit("Use your system package manager to install MiKTeX/XeLaTeX on this platform.")
    tex_bin = Path(os.environ["LOCALAPPDATA"]) / "Programs/MiKTeX/miktex/bin/x64"
    if not (tex_bin / "xelatex.exe").is_file():
        run("winget", "install", "--id", "MiKTeX.MiKTeX", "--exact", "--source", "winget",
            "--scope", "user", "--silent", "--accept-package-agreements",
            "--accept-source-agreements", "--disable-interactivity")
    if not (tex_bin / "xelatex.exe").is_file():
        raise SystemExit(f"MiKTeX was not found at {tex_bin}; check the installation.")
    add_user_path(tex_bin)
    # latexmk needs Perl; Git for Windows already supplies it on this machine.
    if not shutil.which("perl"):
        git_perl = Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Git/usr/bin"
        if (git_perl / "perl.exe").is_file():
            add_user_path(git_perl)
    notify_environment_change()
    run(tex_bin / "initexmf.exe", "--set-config-value=[MPM]AutoInstall=yes")
    run(tex_bin / "miktex.exe", "packages", "update-package-database")
    check = subprocess.run([str(tex_bin / "miktex.exe"), "packages", "check-update"])
    if check.returncode not in (0, 100):
        check.check_returncode()
    run(tex_bin / "miktex.exe", "packages", "update")
    if not (tex_bin / "latexmk.exe").is_file():
        run(tex_bin / "miktex.exe", "packages", "install", "latexmk")
    version = run(tex_bin / "xelatex.exe", "--version", capture=True).stdout
    packages = run(tex_bin / "miktex.exe", "packages", "list",
                   "--template={id}\t{version}\t{versionDate}\t{isInstalled}", capture=True).stdout
    record = ROOT / "build/toolchain"
    record.mkdir(parents=True, exist_ok=True)
    (record / "installation.json").write_text(json.dumps({
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "distribution": "MiKTeX", "engine": "XeLaTeX", "shared_bin": str(tex_bin),
        "version_output": version.strip(),
        "scope": "current Windows user; all projects",
    }, indent=2) + "\n", encoding="utf-8")
    (record / "packages.tsv").write_text(packages, encoding="utf-8")
    print(version.splitlines()[0])
    if shutil.which("perl"):
        print(run(tex_bin / "latexmk.exe", "-v", capture=True).stdout.strip())
    else:
        print("XeLaTeX is ready. Install Perl to use latexmk on this machine.")
    print(f"Shared installation: {tex_bin}\nRestart existing terminals to reload PATH.")


if __name__ == "__main__":
    main()
