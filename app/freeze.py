from flask_frozen import Freezer
from run import app

DEBUG = True
FREEZER_IGNORE_404_NOT_FOUND = True

freezer = Freezer(app)

if __name__ == "__main__":
  freezer.freeze()
