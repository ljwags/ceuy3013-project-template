# Transportation Geometric Design Project

*This is my final project for *CE-UY 3013 Computing In Civil Engineering*.*
*It demostrates horizontal and vertical alignment procedures for highways and streets*
*according to AASHTO Design Guidelines.*

---

This program calculates the horizontal and vertical alignment of roadways with a given starting point, other raodway characteristics.
The program acts as road builder to determine where the end of the curve should be. All of the specifications can be found in **AASHTO A Policy on Geometric Design of Highways and Streets** most specifically Chapter 3 Elements of Design. This program is designed for U.S. customary units.

Assumptions:
* super elevation is equal to 0.10 which common use for highways with snow and ice cited in Section 3.3.3.2
* side friction factor is equal to 0.15 which is common for a 70 mph highway, this can vary greatly as it accounts for type of vehicle, condition of
roadway, and condition of tires
* one lane is traveling in each direction with no median (no case adjustment factor used)

Inputs:

*Horizontal Alignment*

* x and y coordinate of at startion point of curve
* speed (mph)
* tangent line length (ft)

*Vertical Alignment*

* x and z coordinate of at startion point of curve
* speed (mph)
* grades of back and forward tangents
* type of vertical curve (crest or sag)

Outputs:

*Horizontal Alignment*

* radius of curve
* intersection angle (I)
* point of tangent (PT)
* length of middle ordinate (M)
* external distance (E)
* length of long chord (LC)
* horizontal curve visualization

*Vertical Alignment*

* stopping sight distance
* length of curve
* vertical curve visualization



## Setup

In order to use the program, you have to clone/download this repository,
navigate to the local directory and create a virtual environment with:

```
$ python3 -m venv venv
```

Then, activate the virtual environment:

```
For Linux/Mac OS:
$ source venv/bin/activate

For Windows:
> venv\Scripts\activate
```

Finally, install the required libraries for this program with:

```
$ pip install -r requirements.txt
```


## How to use the program

<img src="https://storage.googleapis.com/nm-static/computing_maloof2_20200927.png" alt="nyu_comp_f20" style="max-height:100px">

Here is how we can analyze the truss above.

First instantiate a new object of ``SimpleTruss``:

```python
>>> truss = SimpleTruss('My first truss')
```

Next, we can add the members:

```python
>>> truss.add_member((0, 0, False), (3, 0, True))
>>> truss.add_member((0, 0, False), (3, 4, True))
```

Let's add a load:

```python
>>> truss.add_load((0,0), (0, -2))
```

Finally we can analyze the truss and print the results:

```python
>>> print(truss.solve())
```
