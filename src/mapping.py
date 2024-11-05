import re
import tempfile
import sys
import os
import argparse


# Define a mapping of Guni keywords to Python commands/functions
GUNI_KEYWORDS = {
    'abs': 'Aakaar',
    'aiter': 'Aiterate',
    'all': 'Sab',
    'and': 'Aur',
    'anext': 'AgleElement',
    'any': 'Koi',
    'ArithmeticError': 'MathsKharab',
    'as': 'Jaise',
    'ascii': 'ascii',
    'assert': 'Pakki',
    'AssertionError': 'GalatLogic',
    'async': 'Jugadu',
    'AttributeError': 'GalatProperty',
    'await': 'Ruk',
    'BaseException': 'AamException',
    'BaseExceptionGroup': 'AamExceptionKaGroup',
    'bin': 'Binary',
    'BlockingIOError': 'InputOutputMeDikkat',
    'bool': 'Dogla',
    'break': 'rukja',
    'breakpoint': 'BreakKaro',
    'BrokenPipeError': 'TodoPipeError',
    'BufferError': 'BufferGhalat',
    'build_class': 'ClassBanao',
    'bytearray': 'ByteArray',
    'bytes': 'bytes',
    'BytesWarning': 'BytesWarning',
    'callable': 'CallKarSaktaHai',
    'ChildProcessError': 'BachaProcessError',
    'chr': 'chr',
    'class': 'Chukdi',
    'classmethod': 'ClassMethod',
    'compile': 'CompileKaro',
    'complex': 'complex',
    'ConnectionAbortedError': 'ConnectionKhatamError',
    'ConnectionError': 'ConnectionGhalatError',
    'ConnectionRefusedError': 'ConnectionNahiBana',
    'ConnectionResetError': 'ConnectionResetError',
    'continue': 'Chalu',
    'copyright': 'copyright',
    'credits': 'credits',
    'debug': 'DebugMode',
    'def': 'setkarde',
    'del': 'Khatam',
    'delattr': 'AttributeKhatamKaro',
    'DeprecationWarning': 'DevaluationHoriSambhalJa',
    'dict': 'dict',
    'dir': 'dir',
    'display': 'Dikhai',
    'divmod': 'divmod',
    'doc': 'Documentation',
    'elif': 'WarnaAgar',
    'Ellipsis': 'ChaloChalo',
    'else': 'Warna',
    'EncodingWarning': 'EncodingWarning',
    'enumerate': 'Ginti',
    'EnvironmentError': 'MaaholError',
    'EOFError': 'EOFError',
    'eval': 'SystemBaithao',
    'except': 'Iskealwa',
    'Exception': 'KhasError',
    'ExceptionGroup': 'KhasErrorGroup',
    'exec': 'ExecKaro',
    'execfile': 'Filechala',
    'FileExistsError': 'FileHiNahiHai',
    'FileNotFoundError': 'FileNahiMili',
    'filter': 'FilterKaro',
    'finally': 'Aakhri',
    'float': 'float',
    'FloatingPointError': 'FloatingGhalatError',
    'for': 'Har',
    'format': 'format',
    'from': 'Se',
    'frozenset': 'frozenset',
    'FutureWarning': 'AaneWalaWarning',
    'GeneratorExit': 'GeneratorBandKaro',
    'get_ipython': 'get_ipython',
    'getattr': 'getattr',
    'global': 'Sabka',
    'globals': 'globals',
    'hasattr': 'hasattr',
    'hash': 'hash',
    'help': 'Madad',
    'hex': 'hex',
    'id': 'id',
    'if': 'agar',
    'import': 'Uthao',
    'ImportError': 'ImportNahiHuaError',
    'ImportWarning': 'ImportWarning',
    'in': 'Andar',
    'IndentationError': 'WordKoSahiJagahLikh',
    'IndexError': 'IndexGhalatError',
    'input': 'input',
    'int': 'int',
    'InterruptedError': 'RukaawatError',
    'IOError': 'IOError',
    'IPYTHON': 'IPythonHain',
    'is': 'Hai',
    'IsADirectoryError': 'DirectoryHaiError',
    'isinstance': 'InstanceKyaHai',
    'issubclass': 'SubClassHaiKya',
    'iter': 'IterKarna',
    'KeyboardInterrupt': 'KeyboardSeRukDiya',
    'KeyError': 'MujheNahiMilaYe',
    'lambda': 'Formula',
    'len': 'KitnaLamba',
    'license': 'license',
    'list': 'list',
    'loader': 'LoaderHai',
    'locals': 'locals',
    'LookupError': 'DekhneGhalatError',
    'map': 'map',
    'max': 'Zyada',
    'MemoryError': 'YaadashGhalatError',
    'memoryview': 'YaadashView',
    'min': 'Kam',
    'ModuleNotFoundError': 'ModuleNahiMilaError',
    'name': 'NaamHai',
    'NameError': 'NaamGalathai',
    'next': 'Agla',
    'None': 'kuchni',
    'nonlocal': 'Bahar',
    'not': 'Nahi',
    'NotADirectoryError': 'DirectoryNahiHaiError',
    'NotImplemented': 'AbhiNahiKiya',
    'NotImplementedError': 'AbhiNahiKiyaError',
    'object': 'Vastav',
    'oct': 'oct',
    'open': 'Khol',
    'or': 'Ya',
    'ord': 'UnicodeOrd',
    'OSError': 'OSError',
    'OverflowError': 'OverFlowGhalatError',
    'package': 'PackageHai',
    'pass': 'Chhod',
    'PendingDeprecationWarning': 'AaneWalaPuranaWarning',
    'PermissionError': 'YeNahiKarSakta',
    'pow': 'Power',
    'print': 'Dikha',
    'ProcessLookupError': 'ProcessDekhNahiPayaError',
    'property': 'property',
    'raise': 'Uthao',
    'range': 'range',
    'RecursionError': 'RecursionGalatError',
    'ReferenceError': 'ReferenceGhalatError',
    'repr': 'repr',
    'ResourceWarning': 'ResourceWarning',
    'return': 'Wapas',
    'reversed': 'Palatde',
    'round': 'round',
    'runfile': 'runfile',
    'RuntimeError': 'RunKarteWaqtDikkat',
    'RuntimeWarning': 'RuntimeWarning',
    'set': 'set',
    'setattr': 'AttributeBanao',
    'slice': 'slice',
    'sorted': 'sortkarde',
    'spec': 'Specification',
    'staticmethod': 'StaticMethod',
    'StopAsyncIteration': 'AsyncRukawat',
    'StopIteration': 'RukawatHona',
    'str': 'str',
    'sum': 'Jod',
    'super': 'super',
    'SyntaxError': 'SyntaxGhalatError',
    'SyntaxWarning': 'SyntaxWarning',
    'SystemError': 'SystemGhalatError',
    'SystemExit': 'SystemExit',
    'TabError': 'TabGhalatError',
    'TimeoutError': 'TimeoutGhalatError',
    'try': 'Koshish',
    'tuple': 'tuple',
    'type': 'type',
    'TypeError': 'TypeGhalatError',
    'UnboundLocalError': 'LocalNahiBoundError',
    'UnicodeDecodeError': 'UnicodeDecodeGhalatError',
    'UnicodeEncodeError': 'UnicodeEncodeGhalatError',
    'UnicodeError': 'UnicodeGhalatError',
    'UnicodeTranslateError': 'UnicodeTranslateGhalatError',
    'UnicodeWarning': 'UnicodeWarning',
    'UserWarning': 'UserWarning',
    'ValueError': 'ValueGhalatError',
    'vars': 'vars',
    'Warning': 'Warning',
    'while': 'Jabtak',
    'with': 'Saath',
    'yield': 'De',
    'ZeroDivisionError': 'ZeroDivisionGhalatError',
    'zip': 'Jodo',
    'False': 'Galat',
    'True': 'Sahi',
    'None': 'None',
    'print': 'dikha',
    '>': 'ZyadaHai',
    '<': 'KamHai',
    '==': 'SameHai',
    '!=': 'NahiSameHai',
    '>=': 'ZyadaHaiKya',
    '<=': 'KamHaiKya',
}