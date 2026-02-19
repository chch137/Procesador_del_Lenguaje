import ply.lex as lex

#REGEXP para hacer pruebas

reserved = (
    'TRUE',
    'FALSE',
    'INT',
    'FLOAT',
    'CHAR',
    'BOOLEAN',
    'VOID',
    'RETURN',
    'IF',
    'ELSE',
    'DO',
    'WHILE',
    'PRINT',
    'NEW',
    'RECORD'
) # Esta correcto

tokens = reserved + (
    # Identificadores y literales
    'ID', 'INT_VALUE', 'FLOAT_VALUE', 'CHAR_VALUE',

    # Operadores
    'PLUS','MINUS','TIMES','DIVIDE',
    'AND','OR','NOT',
    'GT','GE','LT','LE','EQ',
    'ASSIGN',
    'DOT',

    # Separadores
    'LPAREN','RPAREN','LBRACE','RBRACE',
    'COMMA','SEMICOLON',
)

reserved_map = {r.lower(): r for r in reserved}

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'

t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

t_GE = r'>='
t_GT = r'>'
t_LE = r'<='
t_LT = r'<'
t_EQ = r'=='
t_ASSIGN = r'='

t_DOT = r'\.'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'

t_ignore = ' \t\r'


def t_DIVIDE_OR_COMMENT(t):
    r'/\*[\s\S]*?\*/|//[^\n]*|/'
    if t.value == '/':
        t.type = 'DIVIDE'
        return t
    t.lexer.lineno += t.value.count('\n')
    pass

def t_FLOAT_VALUE(t):
    r'(\d+(\.\d+)?e[+-]?\d+)|(\d+\.\d+)'
    t.raw = t.value
    t.value = float(t.value)
    return t

def t_INT_VALUE(t):
    r'0b[01]+|0x[0-9A-F]+|0[0-7]+|0|[1-9][0-9]*'
    t.raw = t.value  # lexema original

    s = t.value
    if s.startswith('0b'):
        t.value = int(s[2:], 2)
    elif s.startswith('0x'):
        t.value = int(s[2:], 16)
    elif s.startswith('0') and s != '0':
        t.value = int(s, 8)
    else:
        t.value = int(s, 10)

    return t

def t_BAD_CHAR(t):
    r"'[^\n']{2,}'"
    print(f"ERROR: literal char inválido {t.value} en línea {t.lineno}")
    pass

def t_CHAR_VALUE(t):
    r"'[^\n']'"
    ch = t.value[1]
    if ord(ch) > 255:
        print(f"ERROR: char fuera de ASCII-extendido {t.value} en línea {t.lineno}")
        return
    return t

def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved_map.get(t.value, 'ID') # Funciona correctamente
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
