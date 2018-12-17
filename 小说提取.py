with open('xs.txt', 'rb') as f:
    xs = f.read().decode()
# xs = " <p>　　骄阳似火，要把世间万物给烤化了一般。</p><p>　　整座城市被钢铁水泥给包裹得密不透风，身体四周就像是缠绕了一层看不见摸不着的丝网，粘稠恶心，撕扯不掉。</p>"
import re

xstq = re.sub(r'<p>|</p>|<div class="read-content j_readContent">|</div>|\s*', '', xs)

print(xstq)
with open('xstq.txt', 'w') as f:
    f.write(xstq)
