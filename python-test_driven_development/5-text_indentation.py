#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these
    characters: ., ? and : .

    text must be a string,
    Otherwise TypeError (text must be a string)
    No space at the beginning or at the end of each printed line.

    Returns a text with : . ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    formatted_text = text.replace('. ', '.  \n').replace('? ', '?  \n').replace(': ', ':  \n')
    
    lines = formatted_text.split('\n')
    
    stripped_lines = [line.strip() for line in lines]
    
    for line in stripped_lines:
        print(line)
