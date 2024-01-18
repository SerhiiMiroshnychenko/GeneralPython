from pythonmonkey import require as js_require

js_lib = js_require('./simple-math')

print(js_lib.add(1, 2))  # 3
print(js_lib.sub(1, 2))  # -1
