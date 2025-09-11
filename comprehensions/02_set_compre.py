# comprehension on sets 

CHAI_LIST  = [
    'elaichi', 'irani', 'akbar',
    'elaichi', 'irani', 'african'
]

unique_list = {chai for chai in CHAI_LIST}
print(unique_list)


more_complex = {
    "name": ["trilochan", "random", "trilo"],
    "fame": ["global","mistral", "astral"],
    "director": ["films","movies", "names"],
    "hello": ["hi","hello","truth"]
}

com_list = {item for keys in more_complex.values() for item in keys }
print(com_list)