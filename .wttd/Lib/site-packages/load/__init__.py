__all__ = ["load"]


import imp
import importlib


def load(name, path):
    """Load and initialize a module implemented as a Python source file and return its module object"""
    if hasattr(importlib, "machinery"):
        loader = importlib.machinery.SourceFileLoader(name, path)
        return loader.load_module()
    return imp.load_source(name, path)
