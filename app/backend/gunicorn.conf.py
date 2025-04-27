import multiprocessing

max_requests = 100000
max_requests_jitter = 50
log_file = "-"
bind = "0.0.0.0"

timeout = 230000


num_cpus = multiprocessing.cpu_count()
workers = (num_cpus * 2) + 1
worker_class = "uvicorn.workers.Javaweh"
