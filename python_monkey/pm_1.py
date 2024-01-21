import pythonmonkey as pm

# a string containing some javascript functions
my_js_code = """
function adder(a,b) {
  return a + b;
}

function subtracter(a,b) {
  return a - b;
}
"""

# put your javascript string inside pm.eval to execute it
pm.eval(my_js_code)

# call the adder function from Python
print(pm.globalThis.adder(1, 2))  # outputs 3
print(pm.globalThis.adder(99, 1))  # outputs 100

# call the subtracter function from Python
print(pm.globalThis.subtracter(1, 2))  # outputs -1
print(pm.globalThis.subtracter(99, 1))  # outputs 98
