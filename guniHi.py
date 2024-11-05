from typing import List, Optional
import sys
import argparse
from src.run import run_guni_file

def main(args: Optional[List[str]] = None) -> int:
    """
    Command line interface for Guni language processor
    
    Args:
        args: Optional command line arguments
        
    Returns:
        int: Exit code (0 for success, 1 for failure)
    """
    parser = argparse.ArgumentParser(description="Guni to Python Translator and Executor")
    parser.add_argument("file", help="Path to .guni file")
    
    if args is None:
        args = sys.argv[1:]
    
    parsed_args = parser.parse_args(args)
    
    if not parsed_args.file.endswith('.guni'):
        print("Error: File must have .guni extension")
        return 1
        
    try:
        run_guni_file(parsed_args.file)
        return 0
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 