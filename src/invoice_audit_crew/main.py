#!/usr/bin/env python
import sys
import warnings
from pathlib import Path
from langchain_openai import ChatOpenAI

from invoice_audit_crew.crew import InvoiceAuditCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

INPUT_DIR = Path(__file__).resolve().parents[2] / "input"
OUTPUT_DIR = Path(__file__).resolve().parents[2] / "output"
LLM_MODEL =  ChatOpenAI(model="gpt-4o")  # or swap to another supported LLM



def run():
    """
    Run the crew for each invoice file in the input folder.
    """
    invoice_files = list(INPUT_DIR.glob("*.pdf")) + list(INPUT_DIR.glob("*.png")) + list(INPUT_DIR.glob("*.jpg"))

    if not invoice_files:
        print(f"No invoice files found in {INPUT_DIR}.")
        return

    for invoice_path in invoice_files:
        inputs = {
            'invoice_path': str(invoice_path),
            'purchase_order_path': str(OUTPUT_DIR / "purchase_order.json"),
            'prior_invoices_log': str(OUTPUT_DIR / "invoice_log.csv"),
        }
        try:
            print(f"[DEBUG] Inputs passed to kickoff: {inputs}")
            print(f"Processing: {invoice_path.name}")
            audit_crew = InvoiceAuditCrew(llm=LLM_MODEL)
            audit_crew.crew().kickoff(inputs=inputs)
        except Exception as e:
            print(f"Error processing {invoice_path.name}: {e}")


def train():
    """
    Train the crew using a single invoice sample.
    Supports optional command-line args:
    1. Number of iterations
    2. Output filename
    """
    inputs = {
        "invoice_path": "data/invoice_sample.pdf"
    }

    # Defaults
    n_iterations = 3
    filename = "training_output.json"

    # Parse command-line args safely
    if len(sys.argv) > 1:
        try:
            n_iterations = int(sys.argv[1])
        except ValueError:
            print("[WARN] Invalid iteration count, using default:", n_iterations)

    if len(sys.argv) > 2:
        filename = sys.argv[2]

    try:
        audit_crew = InvoiceAuditCrew(llm=LLM_MODEL)
        audit_crew.crew().train(
            n_iterations=n_iterations,
            filename=filename,
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        audit_crew = InvoiceAuditCrew(llm=LLM_MODEL)
        audit_crew.crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew using a static input.
    """
    inputs = {
        'invoice_path': 'data/invoice_sample.pdf',
    }
    try:
        audit_crew = InvoiceAuditCrew(llm=sys.argv[2])
        audit_crew.crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    command = sys.argv[1].lower() if len(sys.argv) > 1 else "run"

    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "test":
        test()
    elif command == "replay":
        replay()
    else:
        print(f"Unknown command: {command}")
        print("Usage: python main.py [run|train|test|replay]")
        sys.exit(1)

