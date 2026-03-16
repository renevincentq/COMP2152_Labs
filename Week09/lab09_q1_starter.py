# ============================================================
#  WEEK 09 LAB — Q1: SYSTEM INFORMATION REPORTER
#  COMP2152 — Rene Vincent Quiambao
# ============================================================

import os
import sys
import platform


# --- Helper (provided) — error handling example from Week 06 ---
def display(title, data):
    print(f"\n--- {title} ---")
    for k, v in data.items():
        print(f"  {k:<12} : {v}")


def safe_run(label, func, *args):
    try:
        result = func(*args)
        if result is None:
            print(f"  [!] {label} returned None — missing return?")
            return {}
        return result
    except Exception as e:
        print(f"  [ERROR] {label}: {e}")
        return {}


#   Return a dict with keys: "os", "node", "release", "machine"
#   Use: platform.system(), platform.node(),
#        platform.release(), platform.machine()
def get_system_info():
    sys_info = {
        "OS" : platform.system(), # MacOS (darwin), windows, linux, etc
        "Node" : platform.node(), # network name
        "Release" : platform.release(), # kernal version
        "Machine" : platform.machine() #
    }
    return sys_info


#   Return a dict with keys: "version", "executable", "platform"
#   Use: sys.version, sys.executable, sys.platform
def get_python_info():
    py_info = {
        "Version" : sys.version,
        "Executable" : sys.executable,
        "Platform" : sys.platform
    }
    return py_info


#   Return a dict with keys: "path", "exists", "file_count", "is_directory"
#   Use: os.path.abspath(), os.path.exists(),
#        os.listdir() (count items), os.path.isdir()
def get_directory_info(path):
    dir_info = {
        "Path" : os.path.abspath(path),
        "Exists" : os.path.exists(path),
        "File_count" : len(os.listdir(path)) if os.path.exists(path) else 0,
        "Is_directory" : os.path.isdir(path)
    }
    return dir_info


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  SYSTEM INFORMATION REPORTER")
    print("=" * 60)

    info = safe_run("System Info", get_system_info)
    if info: display("System Info", info)

    info = safe_run("Python Info", get_python_info)
    if info: display("Python Info", info)

    info = safe_run("Directory Info", get_directory_info, ".")
    if info: display("Directory Info for '.'", info)

    print("\n" + "=" * 60)