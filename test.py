# This file is required. Use the same name, "test.py". Below you see an example
# of importing a class from "source.py", instantiating a new object and printing
# that object. Replace the code below with your own.


# Check the Horizontal Alignment of the State Route 18 for example. 
# The inputs are HorizontalAlignment(x-coordinate, y-coordinate, speed, tangent length).

from source import HorizontalAlignment

stateroute18h = HorizontalAlignment(2,5,60,3000)

stateroute18h.solve()

# Now, check the Vertical Alignment of the State Route 18.
# The inputs are HorizontalAlignment(x-coordinate, y-coordinate, grade of back tangent, grade of forward tangent, speed, type of curve).

from source import VerticalAlignment

stateroute18v = VerticalAlignment(2,5,-0.5,0.2,60,'sag')

stateroute18v.solve()
