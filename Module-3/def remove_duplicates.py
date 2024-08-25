import nose.tools
 
def remove_duplicates(lst):
    """
    Returns the given list without duplicates.
    The order of the returned list doesn't matter.
 
    For example:
    - If we call remove_duplicates([1,2,1,3,4]), we'll get [1,2,3,4] in return
    - If we call remove_duplicates([]), we'll get [] in return
 
    Hint(s):
    - Remember, you can create a set from a string, which will remove the duplicate elements
    """
   
    # your code here
    lst = list(set(lst))
    return lst
 
lst = [1, 2, 3, 4, 5, 5]
print(remove_duplicates(lst))