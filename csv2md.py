import csv
import argparse


def csv_to_markdown(input_file, output_file, filter_columns, remove_columns, filter_row, gophish=False):
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    if not rows:
        print("O arquivo CSV está vazio.")
        return

    header = rows[0]
    indices = range(len(header))

    # Filtrando as colunas primeiro, conforme especificado por -fc
    if filter_columns:
        filter_columns = filter_columns.split(',')
        indices = [header.index(col) for col in filter_columns if col in header]

    # Removendo as colunas conforme especificado por -r
    if remove_columns:
        remove_columns = remove_columns.split(',')
        indices = [i for i in indices if header[i] not in remove_columns]

    filtered_rows = [[row[i] for i in indices] for row in rows]

    # Filtrando as linhas conforme especificado por -fr
    if filter_row:
        filtered_rows = [row for row in filtered_rows if filter_row not in row]

    # Se a opção --gophish for ativada, transforma a coluna 'status' em 'clicou' e 'preencheu'
    if gophish:
        status_index = filtered_rows[0].index('status') if 'status' in filtered_rows[0] else -1
        if status_index != -1:
            # Removendo a coluna 'status'
            filtered_rows[0] = [col for col in filtered_rows[0] if col != 'status']
            # Adicionando as colunas 'clicou' e 'preencheu'
            filtered_rows[0].append('clicou')
            filtered_rows[0].append('preencheu')


            # Atualizando as linhas removendo 'status' e adicionando 'clicou' e 'preencheu'
            for row in filtered_rows[1:]:
                status_value = row[status_index]
                row.pop(status_index)  # Removendo o valor da coluna 'status'
                row.append('✅' if (status_value == 'Clicked Link' or status_value == 'Submitted Data')else '❌')  # Clicou
                row.append('✅' if status_value == 'Submitted Data' else '❌')  # Preencheu



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
  python csv2md.py -i dados.csv -o tabela.md
  python csv2md.py -i dados.csv -fc "Nome,Idade" -o tabela.md
  python csv2md.py -i dados.csv -r "Endereço" -o tabela.md
  python csv2md.py -i dados.csv -fc "Nome,Idade" -r "Endereço"
  python csv2md.py -i dados.csv -fr "excluir_essa_string"
  python csv2md.py -i dados.csv --gophish -o tabela.md
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-i", "--input", required=True, help="Caminho do arquivo CSV de entrada.")
    parser.add_argument("-o", "--output", required=False,
                        help="Caminho do arquivo de saída Markdown. Se não fornecido, a saída será impressa na tela.")
    parser.add_argument("-fc", "--filter-column", required=False,
                        help="Nomes das colunas a serem mantidas, separados por vírgula.")
    parser.add_argument("-r", "--remove", required=False,
                        help="Nomes das colunas a serem removidas, separados por vírgula.")
    parser.add_argument("-fr", "--filter-row", required=False,
                        help="String que, se presente em uma linha, removerá essa linha da saída.")
    parser.add_argument("--gophish", action="store_true",
                        help="Transforma a coluna 'status' em 'clicou' e 'preencheu' com checkboxes e remove a coluna 'status'.")
    args = parser.parse_args()

    csv_to_markdown(args.input, args.output, args.filter_column, args.remove, args.filter_row, args.gophish)
