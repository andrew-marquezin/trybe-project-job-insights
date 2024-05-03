from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary_list = [
            int(job["max_salary"])
            for job in self.jobs_list
            if job["max_salary"].isnumeric()
        ]

        return max(max_salary_list)

    def get_min_salary(self) -> int:
        min_salary_list = [
            int(job["min_salary"])
            for job in self.jobs_list
            if job["min_salary"].isnumeric()
        ]

        return min(min_salary_list)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError("job doesn't have salary info")
        min_salary, max_salary = job["min_salary"], job["max_salary"]

        if not isinstance(min_salary, int) or not isinstance(max_salary, int):
            raise ValueError("salary must be a number!")
        if min_salary > max_salary:
            raise ValueError("min salary is higher than max salary")
        return min_salary <= int(salary) <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
