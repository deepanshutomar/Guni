import os
import tempfile
from .trans import translate_guni_to_python

def run_guni_file(file_path):
    """
    Hinglish: Guni file ko read karke Python mein convert karta hai aur execute karta hai
    
    Args:
        file_path (str): Guni file ka path
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            guni_code = file.read()
            
        python_code = translate_guni_to_python(guni_code)
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as temp_file:
            temp_file.write(python_code)
            temp_file_path = temp_file.name
            
        exec(compile(python_code, temp_file_path, 'exec'))
        
        os.remove(temp_file_path)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1) 