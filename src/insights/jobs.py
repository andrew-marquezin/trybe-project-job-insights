from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path) as file:
            file_reader = csv.DictReader(file)
            self.jobs_list = list(file_reader)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        pass

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
