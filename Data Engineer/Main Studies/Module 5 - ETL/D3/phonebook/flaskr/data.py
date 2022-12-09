from flaskr import console

def generate(title = "Loading some data", size=1000, method=None, **params):
  console.info(title)
  data = []
  for n in range(size):
    console.progress(n, size)
    if len(params) == 0:
      data.append(method())
    else:
      data.append(method(**params))
  return data

def map(title="Mapping data", data = [], method=None, **params):
  console.info(title)
  new_data = []
  size = len(data)
  for n, entry in enumerate(data):
    console.progress(n, size)
    if len(params) == 0:
      new_data.append(method(entry))
    else:
      new_data.append(method(entry, **params))
  return new_data
