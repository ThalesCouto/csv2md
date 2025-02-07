# csv2md
CSV to Markdown Converter

Este script converte um arquivo CSV em uma tabela no formato Markdown.

## Instalação

Certifique-se de ter o Python 3 instalado em seu sistema.

Clone este repositório ou baixe o script manualmente.

## Uso

Execute o script com os seguintes parâmetros:

```sh
python csv2md.py -i <arquivo_entrada.csv> [opções]
```

### Parâmetros

| Parâmetro              | Obrigatório | Descrição |
|------------------------|------------|-----------|
| `-i, --input`         | Sim        | Caminho do arquivo CSV de entrada. |
| `-o, --output`        | Não        | Caminho do arquivo de saída Markdown. Se não fornecido, a saída será impressa no terminal. |
| `-fc, --filter-column` | Não        | Lista de colunas a serem mantidas, separadas por vírgula. |
| `-r, --remove`        | Não        | Lista de colunas a serem removidas, separadas por vírgula. |
| `-fr, --filter-row`   | Não        | Remove todas as linhas que contenham a string especificada. |

### Exemplos de Uso

1. Converter um CSV para Markdown e exibir a saída no terminal:
   ```sh
   python csv2md.py -i dados.csv
   ```

2. Converter um CSV para Markdown e salvar em um arquivo:
   ```sh
   python csv2md.py -i dados.csv -o tabela.md
   ```

3. Filtrar colunas específicas:
   ```sh
   python csv2md.py -i dados.csv -fc "c1,c2"
   ```

4. Remover colunas específicas:
   ```sh
   python csv2md.py -i dados.csv -r "Column"
   ```

6. Remover todas as linhas que contenham uma string específica:
   ```sh
   python csv2md.py -i dados.csv -fr "excluir_essa_linha"
   ```

