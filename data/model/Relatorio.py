from sql.queries.Queries import Queries
import textual
from textual.app import App, ComposeResult
from textual.widgets import DataTable
from sql.queries.Queries import Queries
class Relatorio(App):
    CSS = """
    Screen {
        align: center middle;
    }

    DataTable {
        width: 26%;
        height: 38%;
        border: round green;
    }
    """
    def exibir_relatorio(self):
        ROWS = [
            ("ITENS", "VALORES"),
            ("Total de atletas monitorados", Queries().quantidade_total_de_atletas_monitorados()),
            ("Atletas com sintomas", Queries().quantidade_e_porcentagem_de_atletas_com_sintomas()),
            ("Idade média dos atletas", Queries()),
            ("Idade média dos atletas sintomáticos", Queries().idade_media_dos_atletas_dos_sintomaticos_e_assintomaticos()[0]),
            ("Idade média dos atletas assintomáticos", Queries().idade_media_dos_atletas_dos_sintomaticos_e_assintomaticos()[1]),
            ("Temperatura corporal mais alta", Queries().temperatura_corporal_mais_alta_relatada()),
            ("Idade do atleta sintomático mais novo", Queries().idade_do_atleta_mais_novo_e_mais_velho_entre_os_sintomaticos()[1]),
            ("Idade do atleta sintomático mais velho", Queries().idade_do_atleta_mais_novo_e_mais_velho_entre_os_sintomaticos()[0]),
        ]
        return ROWS
    
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        self.exibir_relatorio()
        table = self.query_one(DataTable)
        table.add_columns(*self.exibir_relatorio()[0])
        table.add_rows(self.exibir_relatorio()[1:])