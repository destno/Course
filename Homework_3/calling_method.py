import working_with_string as string
import working_with_lists as lst
import working_with_other_type as other

#string
print(string.find_length("Тест длины"))
print(string.symbol_replace("test", 1))
print(string.builds_string("test build"))
print(string.string_reversed("reversed"))
print(string.get_index_symbol("test"))
print(string.swap_case("swAp Case"))
print(string.repeating_element("tttes"))

#list
print(lst.sum_elem_list([1,2,3,4]))
print(lst.multiplication_elem_list([1,2,3,4], 2))
print(lst.merge_list([1,2,3,4], [9,8,7,6,5]))
print(lst.changing_position_list_items_by_index([1,2,3,4], 2))
print(lst.converting_list_to_integer([1,2,3,4]))
print(lst.removing_duplicates_from_set([1,1,3,4]))

#other
print(other.adding_to_dict({0: 10, 1: 20}, 2, 30))
print(other.combining_dictionaries({0: 10, 1: 20}, {3: 11, 4: 21}, {5: 12, 6: 22}))
print(other.deleting_from_dict({0: 10, 1: 20}, 1))
print(other.exists_key_in_dict({0: 10, 1: 20}, 0))
print(other.create_set([1,2,3,4]))
print(other.removing_elem_from_set({1,2}, 1))
print(other.lenght_set({1,2,3,4}))
print(other.exists_elem_in_set({1,2,3}, 1))
print(other.create_tuple(1, 2))
print(other.unpacking_tuple((1,2,)))
print(other.converting_list_to_tuple_and_add_elem([1,2,3], 4))
print(other.converting_tuple_to_dict(((1,2), (3,4))))
print(other.counting_elem_type_tuple([('a', 'b'), ('1', '2'), 1,2]))