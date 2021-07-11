# quine
s='s=%r;print(s%%s)';print(s%s)

# interactive intron
t='';s='t=input()or t;print(f"t={repr(t)};s={repr(s)};exec(s)#{t}")';exec(s)# 
