"""
Use a stack to check whether or not a string has a balanced set of parantheses

Balanced = ({[]})
Not balanced = {]

"""
from stack import Stack


def isParenBalanced(parenString):
	s = Stack()
	index = 0
	is_balanced = True
	
	parenDict = {"(" : ")", "{" : "}", "[" : "]"}
		
	while is_balanced and index < len(parenString):
		current_paren = parenString[index]
		print(s.get_stack())
		if current_paren in parenDict.values():
			if s.isEmpty() or parenDict[s.pop()] != current_paren:
				is_balanced = False
		else:
			s.push(current_paren)
		
		index+=1
		
	return is_balanced
		
print(isParenBalanced("({[]})"))
print(isParenBalanced("({[]}"))

