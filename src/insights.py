from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    lista = []
    for job in jobs_list:
        if job["job_type"] not in lista:
            if job["job_type"] != "":
                lista.append(job["job_type"])
    return lista


def filter_by_job_type(jobs, job_type):
    all_job_types = []
    for job in jobs:
        if job["job_type"] == job_type:
            all_job_types.append(job)
    return all_job_types


def get_unique_industries(path):
    jobs_list = read(path)
    lista = []
    for job in jobs_list:
        if job["industry"] not in lista:
            if job["industry"] != "":
                lista.append(job["industry"])
    return lista


def filter_by_industry(jobs, industry):
    all_job_industries = []
    for job in jobs:
        if job["industry"] == industry:
            all_job_industries.append(job)
    return all_job_industries


def get_max_salary(path):
    jobs_list = read(path)
    all_salary = []
    for job in jobs_list:
        if job["max_salary"].isdigit():
            all_salary.append(int(job["max_salary"]))
    return max(all_salary)


def get_min_salary(path):
    jobs_list = read(path)
    all_salary = []
    for job in jobs_list:
        if job["min_salary"].isdigit():
            all_salary.append(int(job["min_salary"]))
    return min(all_salary)


def matches_salary_range(job, salary):
    if (
        job.get("min_salary") is None
        or job.get("max_salary") is None
        or type(salary) != int
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError
    elem_range = range(job["min_salary"], job["max_salary"])
    for valid_elem in elem_range:
        if valid_elem == salary:
            return True
    return False


def filter_by_salary_range(jobs, salary):
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
    return []
