import sys
import importlib.util
from pathlib import Path

module_name = "plugin_mod"
file_path = Path(__file__).parent / "plugins" / "plugin_mod.py"

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)

print("I am the app")
