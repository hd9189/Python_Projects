observations = []
i = int(input())
for a in range(i):
  c = input().split()
  observation = {}
  observation["time"] = int(c[0])
  observation["position"] = int(c[1])
  observations.append(observation)

def get_time(dict):
  return dict["time"]


max_speed = 0
prev_t = None
prev_p = None
observations.sort(key = get_time)
for ob in observations:
  t = ob["time"]
  p = ob["position"]

  if prev_t == None:
    prev_t = t
    prev_p = p
    continue
  
  t_diff = t - prev_t
  p_diff = abs(p - prev_p)
  speed = p_diff/t_diff

  if max_speed < speed:
    max_speed = speed
  prev_t = t
  prev_p = p

print(max_speed)