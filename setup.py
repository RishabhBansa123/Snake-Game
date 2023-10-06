from distutils.core import setup
import py2exe

setup(console=['snake.py'],
      options={
          'py2exe': {
              'bundle_files': 1,
              'compressed': True,
              'optimize': 2,
              'includes': ['pygame'],
          }
      },
      data_files=[
          ("assets", ["bg.jpg", "apple.png", "background.mp3", "beep.mp3", "gameover.mp3", "ting.mp3"]),
      ]
)
