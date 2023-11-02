# Code and Solution Documentation

For extracting the password the jar file was decompiled using  Procyon. The obtained java code was converted into python class using a language converter, and when observing the code it was found that the compiler checks if
1. len(s) * 2 == len(cls.lookup)
    - This means that the Password exactly has half the length of the lookup array
2. s[i] == cls.hash(cls.lookup[2 * i], cls.lookup[2 * i + 1])
    - This means that the i-th character of the password is hash(lookup[2 * i], lookup[2 * i + 1])

using the above 2 facts and reverse engineering the password (Code in passcheck.py). It was found that Password is 
- KXRPQQGZWSQQWAKDFRMA