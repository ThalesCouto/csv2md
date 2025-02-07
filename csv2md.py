import csv
import argparse

def csv_to_markdown(input_file, output_file, filter_columns, remove_columns, filter_row):
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    if not rows:
        print("O arquivo CSV está vazio.")
        return

    header = rows[0]
    indices = range(len(header))
    
    if filter_columns:
        filter_columns = filter_columns.split(',')
        indices = [header.index(col) for col in filter_columns if col in header]
    
    if remove_columns:
        remove_columns = remove_columns.split(',')
        indices = [i for i in indices if header[i] not in remove_columns]
    
    filtered_rows = [[row[i] for i in indices] for row in rows]
    
    if filter_row:
        filtered_rows = [row for row in filtered_rows if filter_row not in row]
    
    # Criando a tabela Markdown
    markdown_table = []
    new_header = filtered_rows[0]
    separator = ['-' * len(col) for col in new_header]
    
    markdown_table.append('| ' + ' | '.join(new_header) + ' |')
    markdown_table.append('| ' + ' | '.join(separator) + ' |')
    
    for row in filtered_rows[1:]:
        markdown_table.append('| ' + ' | '.join(row) + ' |')
    
    markdown_output = '\n'.join(markdown_table) + '\n'
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as mdfile:
            mdfile.write(markdown_output)
        print(f"Tabela Markdown salva em {output_file}")
    else:
        print(markdown_output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Converte um arquivo CSV para uma tabela Markdown.",
        epilog="""
Exemplos de uso:
  python script.py -i dados.csv -o tabela.md
  python script.py -i dados.csv -fc "Nome,Idade" -o tabela.md
  python script.py -i dados.csv -r "Endereço" -o tabela.md
  python script.py -i dados.csv -fc "Nome,Idade" -r "Endereço"
  python script.py -i dados.csv -fr "excluir_essa_string"
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-i", "--input", required=True, help="Caminho do arquivo CSV de entrada.")
    parser.add_argument("-o", "--output", required=False, help="Caminho do arquivo de saída Markdown. Se não fornecido, a saída será impressa na tela.")
    parser.add_argument("-fc", "--filter-column", required=False, help="Nomes das colunas a serem mantidas, separados por vírgula.")
    parser.add_argument("-r", "--remove", required=False, help="Nomes das colunas a serem removidas, separados por vírgula.")
    parser.add_argument("-fr", "--filter-row", required=False, help="String que, se presente em uma linha, removerá essa linha da saída.")
    args = parser.parse_args()
    
    csv_to_markdown(args.input, args.output, args.filter_column, args.remove, args.filter_row)
