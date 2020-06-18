def n_gram(target, n):
    return [ target[i:i+n] for i in range(len(target) - n + 1)]

message = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

#print(n_gram(message,1))

#print(n_gram(message,2))

print(n_gram(message.split(' '),2))