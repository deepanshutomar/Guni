# Guni 🐍🇮🇳  
*Guni is a Hindi-inspired programming language based on Python, designed to make coding more accessible and culturally relatable for Hindi speakers.*

## Overview
Guni transforms Python syntax into Hindi equivalents, allowing users to write code in Hindi-inspired keywords while maintaining Python’s functionality. This is perfect for those who want to learn programming with a more relatable syntax or simply add a cultural twist to their coding experience. Guni code is saved in `.guni` files and translated into Python for execution.

## Features
- **Hindi-inspired Keywords**: Use culturally familiar Hindi terms in place of Python keywords (e.g., `print` becomes `chaap`, `for` becomes `Har`).
- **Seamless Translation to Python**: A parser converts Guni syntax to standard Python syntax, enabling smooth execution.
- **Error Handling**: Guni maps many Python errors to their Hindi equivalents for a more immersive experience.
- **Relatable Function Names**: Common Python functions have Hindi-inspired alternatives in Guni (e.g., `abs` becomes `Aakaar`, `input` becomes `Dalo`).

## Installation
To get started with Guni:
1. Clone the repository:
   ```bash
   git clone https://github.com/deepanshutomar/Guni.git
   ```
2. Navigate to the directory:
   ```bash
   cd Guni
   ```
3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## How to Use Guni
1. Write your code in a `.guni` file using Guni's Hindi syntax.
2. Run the Guni interpreter to parse and execute the code:
   ```bash
   python GuniHi.py path/to/yourfile.guni
   ```

### Example Code
Here's a simple program written in Guni:
```guni
dikha("Namaste, duniya!")  # This will print "Namaste, duniya!" in the console

AakaarSeBada = Jod(7, 3)  # Adds 7 and 3 using Guni's Hindi functions
dikha("Jama kar ke:", AakaarSeBada)
```

### Python Equivalent
The above code is equivalent to this in Python:
```python
print("Namaste, duniya!")
sum_result = sum(7, 3)
print("Jama kar ke:", sum_result)
```


## Guni Syntax Mapping
Here is a basic list of some Guni keywords and their Python equivalents:

| Python            | Guni             |
|-------------------|------------------|
| `print`           | `dikhao`         |
| `for`             | `Har`            |
| `and`             | `Aur`            |
| `if`              | `agar`           |
| `def`             | `setkarde`       |
| `import`          | `Uthao`          |

For the full list of mappings, refer to the [mapping.py file](./mapping.xlsx) in this repository.

## Development
Feel free to contribute! Here’s how you can get started:
1. Fork this repository.
2. Create a new branch with a descriptive name:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes.
4. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
5. Push to your branch:
   ```bash
   git push origin feature-name
   ```
6. Open a pull request on the main repository.

### Future Enhancements
- **Error Messages in Hindi**: Enhanced error handling with Hindi messages for a fully immersive experience.
- **Custom Libraries**: Add popular libraries with Guni-specific syntax.
- **Interactive Shell**: Develop an interactive Guni shell for direct command input.

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

## Contributing
We welcome contributions! Check out our [contributing guidelines](./CONTRIBUTING.md) for more information.

## Contact
For any questions or feedback, feel free to reach out:
- Instagram: [@deepanshutomarg](https://instagram.com/deepanshutomarg)

Enjoy coding in Guni! 🎉 
