# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints (Not always necessary) 
    # Determine a Logical way to solve the problem
        #Write each step out English
        #Write each step out in Python-esse (sudo-code)
    # Invoke and Test Your Function

# In this coding challenge, you have to create a function that will identify the basic data type of the given input. The function should identify the input data as one of the following categories: 'string', 'integer', 'float', or 'boolean'.
# Input:

# input_data - The input data can be of any basic Python data type, including strings, integers, floats, or booleans.
# Output:

# Return a string representing the identification of the input data.
# Examples:


#basic_data_type_identifier("hello") # returns "string"
#basic_data_type_identifier(42) # returns "integer"
#basic_data_type_identifier(3.14) # returns "float"
#basic_data_type_identifier(True) # returns "boolean"

"""
input types: string, integer, float, boolean

def basic_data_type(input_data):

output: type of input

constraints: 1 data type

"""

def basic_data_type(input_data):
    data_type = type(input_data)
    if data_type == str:
        return "string"

    if type(input_data) == int:
        return "integer"


    if type(input_data) == float:
        return "float"


    if type(input_data) == bool:
        return "boolean"


print(basic_data_type(123))

# Tom's Answer Below (Does the Same Thing)

# def basic_data_type(input_data):
#     data_type = type(input_data)
#     if data_type == str:
#         return "string"

#     elif type(input_data) == int:
#         return "integer"


#     elif type(input_data) == float:
#         return "float"


#     else:
#         return "boolean"


# print(basic_data_type(123))

#  Dylan's Version
# def what_data_type(data_type):
#     return 'string' if isinstance(data_type,str) else 'float' if isinstance(data_type,float) else 'boolean' if isinstance(data_type,bool) else 'integer'