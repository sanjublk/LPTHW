#EXERCISE 24 More Practice

print("lets practice everything")
print('you \'d need to know \'bout escapes with \\ that do:')
print("\n newlines and \t tabs.")

poem = """
\t The lovely world 
with logic so firmly planted 
cannot discern \n the needs of love
nor comprehend passion from intuition and requires an explanation
\n\t\t  where there is none.
"""

print("-----------------")
print(poem)
print("-----------------")

five = 10 - 2 + 3 - 6
print(f"this should be five: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 100000
beans, jars, crates = secret_formula(start_point)
print("with a starting point of: {}".format(start_point))
print(f"we have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("we can also do that this way")
formula = secret_formula(start_point)
print("we have {} beans, {} jars and {} crates.".format(*formula))
