#creating a tuple
original_tuple=(1,3,6)
#adding a new element to the tuple
new_element=9
updated_tuple=original_tuple +(new_element,)
#removing an element in the tuple 
updated_tuple=original_tuple[:1]+original_tuple[3:]
#modifing an element in the tuple
modified_element=5
updated_tuple=original_tuple[:1] +(modified_element,)+original_tuple[3:]
print(updated_tuple)
