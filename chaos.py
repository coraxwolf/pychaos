import pygame as pg
from utilities import roll_die

# Point Class
class Point:
  x, y = 0, 0
  def __init__(self, x, y):
    self.x = x
    self.y = y

# Anchors
class Anchor:
  point = Point(0, 0)
  values = []
  def __init__(self, point):
    self.point = point
  def set_values(self, values):
    self.values = values
  def draw(self, screen):
    pg.draw.circle(screen, "blue", (self.point.x, self.point.y), 2)

def set_anchor_values(anchors):
  count = len(anchors)
  match count:
    case 3:
      anchors[0].set_values([1,2])
      anchors[1].set_values([3,4])
      anchors[2].set_values([5,6])
    case 4:
      anchors[0].set_values([1,3])
      anchors[1].set_values([2,4])
      anchors[2].set_values([5]) 
      anchors[3].set_values([6])
    case 5:
      anchors[0].set_values([1,2])
      anchors[1].set_values([3])
      anchors[2].set_values([4])
      anchors[3].set_values([5])
      anchors[4].set_values([6])
    case 6:
      anchors[0].set_values([1])
      anchors[1].set_values([2])
      anchors[2].set_values([3])
      anchors[3].set_values([4])
      anchors[4].set_values([5])
      anchors[5].set_values([6])
    case _:
      print("Invalid number of anchors")
      exit()
  
def find_midpoint(p1: Point, p2: Point):
  x = (p2.x + p1.x) / 2
  y = (p2.y + p1.y) / 2
  return Point(x, y)

pg.init()
screen = pg.display.set_mode((1024, 768))
pg.display.set_caption("Patterns of Chaos")
clock = pg.time.Clock()
running = True
simulation = False
anchors_set = False
anchors = []
iterations = 0
last_dot = Point(0, 0)

screen.fill("black")

while running:
  # Draw Anchors
  for anchor in anchors:
    anchor.draw(screen)
  
  # Check if Simulation is running
  if simulation == True:
    # Run Simulation
    iterations += 1
    roll = roll_die()
    if last_dot.x == 0 and last_dot.y == 0:
      midpoint = Point(anchors[0].point.x, anchors[0].point.y)
      match len(anchors):
        case 3:
          midpoint = find_midpoint(anchors[0].point, anchors[2].point)
        case 4:
          midpoint = find_midpoint(anchors[0].point, anchors[3].point)
        case 5:
          midpoint = find_midpoint(anchors[0].point, anchors[4].point)
        case 6:
          midpoint = find_midpoint(anchors[0].point, anchors[5].point)
      print("First Point: (" + str(midpoint.x) + ", " + str(midpoint.y) + ")")
      pg.draw.circle(screen, "white", (midpoint.x, midpoint.y), 2)
      last_dot = midpoint
    else:
      point = Anchor(Point(last_dot.x, last_dot.y))
      for anchor in anchors:
        for value in anchor.values:
          if value == roll:
            point = anchor.point
            break
      midpoint = find_midpoint(last_dot, point)
      pg.draw.circle(screen, "white", (midpoint.x, midpoint.y), 2)
      
      last_dot = midpoint
  
  # Draw Status Bar
  game_text = ""
  if anchors_set == False:
    game_text = "Mode: Place Anchors -- Click to place Anchor " + str(len(anchors) + 1) + "/6 -- Press Spacebar to start simulation after at least 3 anchors are placed -- Press 'Q' to quit.\n"
  else:
    if simulation == False:
      game_text = "Paused: Press Spacebar to start Simulation -- Press 'Q' to quit. -- Last Iteration: " + str(iterations) + "\n"
    else:
      game_text = "Running: Iteration " + str(iterations) + " -- Press Spacebar to pause Simulation -- Press 'Q' to quit. Last Placed dot ("+ str(last_dot.x) + ", " + str(last_dot.y) + ")\n"
  
  status_block = pg.draw.rect(screen, "white", (0, 0, 1024, 20), 0)
  status_text = pg.font.SysFont("Arial", 12).render(game_text, True, "black")
  screen.blit(status_text, (10, 0))
  
  # Update Display
  pg.display.flip()
  clock.tick(60)
  
  # Check for Events
  for event in pg.event.get():
    # Check for Quit event
    if event.type == pg.QUIT:
      running = False
    if event.type == pg.KEYDOWN:
      print("Key Press Detected")
      if event.key == pg.K_q:
        running = False
      if simulation == False:
        if event.key == pg.K_SPACE:
          if len(anchors) >= 3:
            set_anchor_values(anchors)
            anchors_set = True
          else:
            print("Not enough anchors placed to start simulation")
            break
          simulation = True
      else:
        if event.key == pg.K_SPACE:
          simulation = False
    # Place Anchors
    if event.type == pg.MOUSEBUTTONDOWN: 
      if simulation == False and anchors_set == False and len(anchors) < 6:
        if len(anchors) == 5:
          anchor = Anchor(Point(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]))
          anchors.append(anchor)
          anchors_set = True
        else:
          anchor = Anchor(Point(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]))
          anchors.append(anchor)
# End of Event Loop

# Exit Application
pg.quit()