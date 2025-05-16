from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from invoice_audit_crew.tools.custom_tool import ExtractTextFromInvoiceTool
from invoice_audit_crew.tools.custom_tool import SaveReportTool
import yaml
from pathlib import Path


@CrewBase
class InvoiceAuditCrew:
    """InvoiceAuditCrew crew """

    def __init__(self, llm):
        self.llm = llm  # store the LLM to use for all agents
        print("[DEBUG] InvoiceAuditCrew.__init__ called with llm:", type(llm).__name__)
        base_path = Path(__file__).resolve().parent
        config_dir = base_path / "config"

        with open(config_dir / "agents.yaml") as f:
            self.agents_config = yaml.safe_load(f)
        with open(config_dir / "tasks.yaml") as f:
            self.tasks_config = yaml.safe_load(f)

    @agent
    def extractor(self) -> Agent:
        print("[DEBUG] Initializing extractor agent...")
        cfg = self.agents_config['extractor']
        print(f"[DEBUG] extractor config raw: {cfg}")

        try:
            return Agent(
                role=cfg['role'],
                goal=cfg['goal'],
                backstory=cfg['backstory'],
                llm=self.llm,
                tools=[ExtractTextFromInvoiceTool()],
                verbose=True
            )
        except Exception as e:
            print("[ERROR] Failed to initialize extractor Agent:", e)
            raise

    @agent
    def categorizer(self) -> Agent:
        cfg = self.agents_config['categorizer']
        return Agent(
            role=cfg['role'],
            goal=cfg['goal'],
            backstory=cfg['backstory'],
            llm=self.llm,
            verbose=True
        )

    @agent
    def validator(self) -> Agent:
        cfg = self.agents_config['validator']
        return Agent(
            role=cfg['role'],
            goal=cfg['goal'],
            backstory=cfg['backstory'],
            llm=self.llm,
            verbose=True
        )

    @agent
    def summarizer(self) -> Agent:
        cfg = self.agents_config['summarizer']
        return Agent(
            role=cfg['role'],
            goal=cfg['goal'],
            backstory=cfg['backstory'],
            llm=self.llm,
            tools=[SaveReportTool()],
            verbose=True
        )

    @task
    def extract_invoice_data_task(self) -> Task:
        print("[DEBUG] extract_invoice_data_task registered with variable template")
        return Task(
            config=self.tasks_config['extract_invoice_data_task'],
            input_variables=["invoice_path"]
        )

    @task
    def categorize_line_items_task(self) -> Task:
        return Task(
            config=self.tasks_config['categorize_line_items_task'],
        )

    @task
    def audit_invoice_task(self) -> Task:
        return Task(
            config=self.tasks_config['audit_invoice_task'],
        )

    @task
    def generate_summary_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_summary_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.extractor(),
                self.categorizer(),
                self.validator(),
                self.summarizer()
            ],
            tasks=[
                self.extract_invoice_data_task(),
                self.categorize_line_items_task(),
                self.audit_invoice_task(),
                self.generate_summary_task()
            ],
            process=Process.sequential,
            verbose=True
        )

