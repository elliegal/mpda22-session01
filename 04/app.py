from flask import Flask
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)

"""
    How to create inputs and outputs for hops.
    
    Hops Inputs should match the number of Hops inputs
    Hops Outputs should match the number of items that the functions returns 
"""


@hops.component(
    "/mycomponent",
    name = "MyComponent",
    inputs=[
        hs.HopsString("Name", "N", "Provide your name"),
        hs.HopsInteger("Age", "A", "Provide your age"),
        hs.HopsInteger("Height", "H", "Provide your height in cm")
    ],
    outputs=[
       hs.HopsString("Text","T","Print name, age and height")
    ]
)
def printNameAgeAndHeight(name, age, height):
    text="My name is {}, I am {} years old and I am {}cm tall.".format(name, age, height)
    return text


if __name__== "__main__":
    app.run(debug=True)