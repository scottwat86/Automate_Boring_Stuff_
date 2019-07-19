# errorExample.py

def spam():
    bacon()
def bacon():
    raise Exception('This is the error message.')

spam()

'''OUTPUT
---------------------------------------------------------------------------
Exception                                 Traceback (most recent call last)
<ipython-input-3-7b02ca9e2b9d> in <module>()
----> 1 spam()

<ipython-input-1-080a02573cfb> in spam()
      1 def spam():
----> 2     bacon()

<ipython-input-2-6431c8b570e5> in bacon()
      1 def bacon():
----> 2     raise Exception('This is the error message.')

Exception: This is the error message.
'''
