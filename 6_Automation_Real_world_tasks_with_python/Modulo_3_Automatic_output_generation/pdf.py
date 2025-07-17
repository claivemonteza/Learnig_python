from reportlab.platypus import SimpleDocTemplate

script_dir = os.path.dirname(os.path.abspath(__file__))

report = SimpleDocTemplate("/report.pdf")

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}
