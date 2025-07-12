#!/usr/bin/env python3
"""
Test runner for Python code snippets
Verifies that all code snippets execute without errors
"""

import os
import sys
import importlib.util


def run_snippet(filepath):
    """Run a Python snippet and return success/failure"""
    try:
        # Get the module name from the filepath
        module_name = os.path.splitext(os.path.basename(filepath))[0]
        
        # Load and execute the module
        spec = importlib.util.spec_from_file_location(module_name, filepath)
        module = importlib.util.module_from_spec(spec)
        
        # Redirect stdout to capture output
        import io
        from contextlib import redirect_stdout
        
        with redirect_stdout(io.StringIO()) as output:
            spec.loader.exec_module(module)
        
        return True, output.getvalue()
    except Exception as e:
        return False, str(e)


def test_all_snippets():
    """Test all snippets in all playlist directories"""
    playlist_dirs = ["01-python-one-liners", "02-python-comprehensions"]
    
    all_passed = 0
    all_failed = 0
    
    for snippets_dir in playlist_dirs:
        if not os.path.exists(snippets_dir):
            print(f"Directory {snippets_dir} not found!")
            continue
        
        # Get all Python files in the directory
        python_files = [f for f in os.listdir(snippets_dir) 
                       if f.endswith('.py')]
        
        if not python_files:
            print(f"No Python files found in {snippets_dir}")
            continue
        
        print(f"Testing {snippets_dir}: {len(python_files)} Python snippets...")
        
        passed = 0
        failed = 0
        
        for filename in sorted(python_files):
            filepath = os.path.join(snippets_dir, filename)
            print(f"  {filename}... ", end="")
            
            success, output = run_snippet(filepath)
            
            if success:
                print("✅ PASSED")
                passed += 1
            else:
                print("❌ FAILED")
                print(f"    Error: {output}")
                failed += 1
        
        print(f"  {snippets_dir}: {passed} passed, {failed} failed")
        print()
        
        all_passed += passed
        all_failed += failed
    
    print("="*50)
    print(f"Overall Results: {all_passed} passed, {all_failed} failed")
    print(f"Success rate: {all_passed/(all_passed+all_failed)*100:.1f}%")
    
    return all_failed == 0


if __name__ == "__main__":
    success = test_all_snippets()
    sys.exit(0 if success else 1) 