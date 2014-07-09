from .controllers import primary
from .controllers import demo_loops
import inputs, outputs
import rospy
from basic_head_api.msg import MakeFaceExpr

class SmartTrack2:
  """
  Tracks pivison input and produces random, but smooth expressions using
  basic_head_api.
  """

  def step(self, dt):
    primary.point_head_at(self.face_input.location)
    self.exprs.step(dt)

  def __init__(self):
    self.face_input = inputs.get_instance("PiVision")
    self.neck_output = outputs.get_instance("neck_euler")
    self.exprs = demo_loops.SmoothExpressions(
      rospy.Publisher("make_face_expr", MakeFaceExpr, queue_size=2)
    )