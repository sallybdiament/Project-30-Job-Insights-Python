from typing import Union, List, Dict
from src.insights.jobs import read
# from jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    try:
        all_jobs = read(path)
        all_max_salaries = []
        for job in all_jobs:
            if job["max_salary"] != '' and job["max_salary"] != 'invalid':
                all_max_salaries.append(int(job["max_salary"]))
        return max(all_max_salaries)
    except FileNotFoundError:
        raise FileNotFoundError(f"Not found file: {path}")


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    try:
        all_jobs = read(path)
        all_min_salaries = []
        for job in all_jobs:
            if job["min_salary"] != '' and job["min_salary"] != 'invalid':
                all_min_salaries.append(int(job["min_salary"]))
        return min(all_min_salaries)
    except FileNotFoundError:
        raise FileNotFoundError(f"Not found file: {path}")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        sal = int(salary)
        max_salary = int(job["max_salary"])
        min_salary = int(job["min_salary"])
        if min_salary > max_salary:
            raise ValueError
    except (TypeError, ValueError, KeyError):
        raise ValueError("Esta vaga não está com os valores corretos")
    else:
        if min_salary <= sal and sal <= max_salary:
            return True
        else:
            return False


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    result = []
    for job in jobs:
        try:
            valid_job = matches_salary_range(job, salary)
        except (TypeError, ValueError, KeyError):
            continue
        else:
            if valid_job:
                result.append(job)
    return result
