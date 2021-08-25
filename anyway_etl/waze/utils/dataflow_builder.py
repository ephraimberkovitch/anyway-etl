import os
import dataflows as DF


class DataflowBuilder:
    def __init__(self, parser_retriever):
        self.parser_retriever = parser_retriever

    @property
    def parent_directory(self):
        return os.path.dirname(os.path.dirname(__file__))

    def get_items(self, waze_data: dict, field: str) -> list:
        return waze_data.get(field, [])

    def build_dataflow(self, waze_data: dict, field: str) -> DF.Flow:
        parser = self.parser_retriever.get_parser(field)

        output_path = os.path.join(self.parent_directory, f"waze_{field}")

        return DF.Flow(
            self.get_items(waze_data, field), parser, DF.dump_to_path(output_path)
        )
