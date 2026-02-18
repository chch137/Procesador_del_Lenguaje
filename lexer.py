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
t_DIVIDE = r'/'

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

t_ignore = ' \t'


def t_comment_single(t):
    r'//[^\n]*'
    pass

def t_comment_multi(t):
    r'/\*[\s\S]*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

def t_FLOAT_VALUE(t):
    r'(\d+(\.\d+)?e[+-]?\d+)|(\d+\.\d+)'
    # t.value = float(t.value)
    return t

def t_INT_VALUE(t):
    r'0b[01]+|0x[0-9A-F]+|0[0-7]+|0|[1-9][0-9]*'
    # t.value = int(t.value)
    return t

def t_CHAR_VALUE(t):
    r"\'([^\\\n\']|\\.)\'"
    return t

def t_ID(t):
    r'[A-Za-z_]\w*'
    t.type = reserved_map.get(t.value, 'ID') # Funciona correctamente
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
