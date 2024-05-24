import shutil

x = 0
src = "rock.jpg"

while(True):
  x += 1
  dst = "rock" + str(x) + ".jpg"
  shutil.copy(src, dst)