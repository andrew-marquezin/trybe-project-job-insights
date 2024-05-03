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
        job_types = set(job["job_type"] for job in self.jobs_list)
        return job_types

    def filter_by_multiple_criteria(
        self, jobs: List[dict], filter: dict
    ) -> List[dict]:
        if not isinstance(filter, dict):
            raise TypeError("'filter' must be a dictionary!")

        filtered_jobs = []
        for job in jobs:
            if all(job[key] == value for key, value in filter.items()):
                filtered_jobs.append(job)
        return filtered_jobs
