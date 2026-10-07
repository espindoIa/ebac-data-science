"""Executa os notebooks com a base incluída, sem gravar saídas ou abrir gráficos."""

import contextlib
import io
import json
import os
from pathlib import Path
import unittest

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]


def run_notebook(name):
    notebook = json.loads((ROOT / name).read_text(encoding="utf-8"))
    namespace = {"__name__": "__main__"}
    previous = Path.cwd()
    try:
        os.chdir(ROOT)
        with contextlib.redirect_stdout(io.StringIO()):
            for index, cell in enumerate(notebook["cells"]):
                if cell["cell_type"] == "code":
                    source = "".join(cell["source"])
                    exec(compile(source, f"{name}:cell-{index}", "exec"), namespace)
                    plt.close("all")
    finally:
        os.chdir(previous)
        plt.close("all")
    return namespace


class NotebookTests(unittest.TestCase):
    def test_module14_uses_included_csv_without_losing_churn(self):
        result = run_notebook("Profissao Cientista de Dados M14 Pratique.ipynb")
        frame = result["df"]
        self.assertIn("gender", frame.columns)
        self.assertTrue(frame["churn"].notna().all())
        self.assertEqual(set(frame["churn"].unique()), {0, 1})

    def test_module15_keeps_requested_tenure_labels(self):
        result = run_notebook("Profissao Cientista de Dados M15 Pratique.ipynb")
        categories = result["df_tratado"]["faixa_tenure"].cat.categories.tolist()
        self.assertEqual(categories, ["≤12", "13-24", "25-36", "37-48", "49-60", "61-72"])


if __name__ == "__main__":
    unittest.main()
