from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    try:
        all_jobs = read(path)
        all_industries = set()
        for job in all_jobs:
            all_industries.add(job["industry"])
        if "" in all_industries:
            all_industries.remove("")
        return all_industries
    except FileNotFoundError:
        raise FileNotFoundError(f"Not found file: {path}")


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    jobs_by_industry = [x for x in jobs if x["industry"] == industry]
    return jobs_by_industry
