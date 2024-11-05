import re
from .mapping import GUNI_KEYWORDS

def translate_guni_to_python(guni_code):
    """
    Hinglish: Guni code ko Python code mein convert karta hai
    
    Args:
        guni_code (str): Guni language mein likha hua code
        
    Returns:
        str: Python code mein convert kiya hua code
    """
    python_code = guni_code
    
    for guni_keyword, python_keyword in GUNI_KEYWORDS.items():
        pattern = r'\b' + re.escape(python_keyword) + r'\b'
        python_code = re.sub(pattern, guni_keyword, python_code)
        
    return python_code 