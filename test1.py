import js2py

context = js2py.EvalJs()

with open('test.js','r',encoding='utf-8') as f:
    context.execute(f.read())

print(context.add())
