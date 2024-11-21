import tkinter as tk
from tkinter import ttk
import threading
from pipeline import Pipeline
from stage import Stage
from status import Status

class PipelineUI:

    def __init__(self, pipeline: Pipeline):
        self.pipeline = pipeline
        self.root = tk.Tk()
        self.root.title("PYPE_LINE")
        self.root.geometry("600x400")
        self.root.iconbitmap("icon2.ico")
        self.is_running = False

        self.tree = ttk.Treeview(self.root, columns=("Stage", "Status", "Elapsed Time"), show="headings", height=15)
        self.tree.heading("Stage", text="Stage")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Elapsed Time", text="Elapsed Time (s)")
        self.tree.pack(fill=tk.BOTH, expand=True)

        for stage in self.pipeline.stages:
            self.tree.insert("", tk.END, iid=stage.name, values=(stage.name, stage.status, "0"))

        self.run_button = tk.Button(self.root, text="Run Pipeline", command=self.run_pipeline)
        self.run_button.pack(pady=10)


    def update_ui(self, stage: Stage, status: str):
        elapsed_time = f"{stage.elapsed_time:.2f}" if status in [Status.RUNNING, Status.SUCCESS, Status.FAILED] else "0.00"
        self.tree.item(stage.name, values=(stage.name, status, elapsed_time))


    def run_pipeline(self):
        if self.is_running:
            return

        self.is_running = True
        self.run_button.config(state=tk.DISABLED)
        threading.Thread(target=self.pipeline.run, args=(self.update_ui, self.pipeline_finished)).start()


    def pipeline_finished(self):
        self.is_running = False
        self.run_button.config(state=tk.NORMAL)


    def start(self):
        self.root.mainloop()