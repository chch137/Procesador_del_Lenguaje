import sys
from lexer import lexer

def find_column(data, lexpos):
    last_nl = data.rfind('\n', 0, lexpos)
    return lexpos - (last_nl + 1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file.lava>")
        sys.exit(1)

    in_path = sys.argv[1]
    with open(in_path, 'r', encoding='utf-8') as f:
        data = f.read()

    lexer.lineno = 1
    lexer.input(data)

    out_path = in_path.rsplit('.', 1)[0] + '.token'

    with open(out_path, 'w', encoding='utf-8') as out:
        for tok in iter(lexer.token, None):
            col_start = find_column(data, tok.lexpos)
            col_end = col_start + len(tok.value)  # correcto: longitud del lexema
            out.write(f"{tok.type}, {tok.value}, {tok.lineno}, {col_start}, {col_end}\n")

if __name__ == "__main__":
    main()
