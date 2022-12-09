import logging

#def initialize_logging():
logging.basicConfig(level=logging.INFO)

def info(*data):
  logging.info(*data)

def warn(*data):
  logging.warning(*data)

def progress(current, end, length = 50):
  percent = current / end
  bar = ("*" * round(percent * length)) + ("-" * round((1 - percent) * length))
  progress=f"\r\tLoading... |{bar}| {round(percent * 100, 2)}% "

  print(progress, end="\r")

  if current + 1 == end:
    clear_space = " " * (len(progress) + 10)
    print(f"{clear_space}", end="\r")
    print(f"\tCompleted |{bar}| 100%", end="\r\n")
