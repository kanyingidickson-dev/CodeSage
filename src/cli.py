import argparse
import sys
from .analyze import Analyzer

def main():
    parser = argparse.ArgumentParser(description="CodeSage CLI")
    parser.add_argument("--input", type=str, help="Code string to analyze")
    parser.add_argument("--file", type=str, help="Path to file to analyze")
    
    args = parser.parse_args()
    
    if not args.input and not args.file:
        print("Please provide --input or --file")
        sys.exit(1)
        
    code = args.input
    if args.file:
        with open(args.file, 'r') as f:
            code = f.read()
            
    analyzer = Analyzer()
    results = analyzer.analyze_snippet(code)
    print(results)

if __name__ == "__main__":
    main()
