import subprocess

class ProgramOpener:
    def __init__(self, program_path):
        self.program_path = program_path

    def open_program(self):
        try:
            subprocess.Popen(self.program_path)
            print(f"Successfully opened {self.program_path}")
        except FileNotFoundError:
            print(f"Program not found at {self.program_path}")
        except Exception as e:
            print(f"Error occurred while opening program: {str(e)}")


